<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item> <i class="el-icon-lx-calendar"></i> 进出口工作时间计划表 </el-breadcrumb-item>
                <el-breadcrumb-item>出口计划表</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="form-box">
                <el-form ref="form" :model="form" label-width="120px">
                    <el-form-item>
                        <el-select
                            v-model="selectedId"
                            filterable
                            placeholder="船舶名 必填项！！！"
                            class="handle-select mr10"
                            @change="selectchange"
                        >
                            <el-option v-for="item in shipdata" :key="item.id" :label="item.ship_name" :value="item.id"></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="预计工作效率及出口数量 : " label-width="200px">
                        <el-row>
                            <el-col span="8">
                                <el-input v-model="form.inp" placeholder="ERL"></el-input>
                            </el-col>
                            <el-col span="8">
                                <el-input v-model="form.incount" placeholder="出口数量"></el-input>
                            </el-col>
                        </el-row>
                    </el-form-item>
                    <el-form-item label="作业线数量 : ">
                        <el-input v-model="form.count" placeholder="数量"></el-input>
                    </el-form-item>
                    <el-form-item label="作业线开工时间 : ">
                        <el-date-picker
                            type="date"
                            placeholder="选择日期"
                            v-model="form.date"
                            value-format="yyyy-MM-dd"
                            style="width: 100%"
                        ></el-date-picker>
                        <el-time-picker
                            placeholder="选择时间"
                            v-model="form.time"
                            value-format="HH:mm:ss"
                            style="width: 100%"
                        ></el-time-picker>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="info" @click="onGenerate">生成</el-button>
                        <el-button type="info" @click="onClear">清空</el-button>
                    </el-form-item>

                    <el-form-item>
                        <el-button type="primary" @click="onSubmit">确认</el-button>
                        <el-button>取消</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </div>
        <div class="container">
            <el-table :data="tableData" border class="table" header-cell-class-name="table-header">
                >
                <!-- <el-table-column type="selection" width="55" align="center"></el-table-column> -->
                <el-table-column prop="id" label="ID" width="55" align="center"></el-table-column>
                <el-table-column prop="bw" label="岸桥"></el-table-column>
                <el-table-column label="作业数量">
                    <template scope="scope">
                        <span v-show="!scope.row.edit">{{ scope.row.incount }}</span>
                        <el-input v-show="scope.row.edit" v-model="scope.row.incount"></el-input>
                    </template>
                </el-table-column>
                <el-table-column>
                    <template scope="scope">
                        <el-button v-show="!scope.row.edit" type="primary" @click="scope.row.edit = true" size="small" icon="edit"
                            >编辑</el-button
                        >
                        <el-button v-show="scope.row.edit" type="success" @click="onSub(scope.row.id)" size="small" icon="check"
                            >完成</el-button
                        >
                    </template>
                </el-table-column>
                <el-table-column prop="ph" label="准备作业"></el-table-column>
                <el-table-column prop="st" label="开工时点"></el-table-column>
                <el-table-column prop="ht" label="作业时长"></el-table-column>
                <el-table-column prop="zsc" label="总时长"></el-table-column>
                <el-table-column prop="jjb" label="交接班"></el-table-column>
                <el-table-column prop="kcg" label="开仓盖"></el-table-column>
                <el-table-column prop="tgcf" label="停工吃饭"></el-table-column>
                <el-table-column prop="cxx" label="超限箱"></el-table-column>
                <el-table-column prop="jczh" label="进出转换"></el-table-column>
                <el-table-column prop="wgsd" label="完工时点"></el-table-column>
                <el-table-column label="操作" width="180" align="center">
                    <template slot-scope="scope">
                        <el-button type="text" icon="el-icon-edit" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                        <el-button type="text" icon="el-icon-delete" class="red" @click="handleDelete(scope.$index, scope.row)"
                            >删除</el-button
                        >
                    </template>
                </el-table-column>
            </el-table>
        </div>

        <!-- 编辑弹出框 -->
        <el-dialog title="编辑" :visible.sync="editVisible" width="30%">
            <el-form ref="form" :model="edit_form" label-width="70px">
                <el-form-item label="ID" hidden>
                    <el-input v-model="form.id"></el-input>
                </el-form-item>
                <el-form-item label="岸桥">
                    <el-input v-model="form.bw"></el-input>
                </el-form-item>
                <el-form-item label="作业数量">
                    <el-input v-model="form.incount"></el-input>
                </el-form-item>
                <el-form-item label="准备作业">
                    <el-input v-model="form.ph"></el-input>
                </el-form-item>
                <el-form-item label="开工时点">
                    <el-input v-model="form.st"></el-input>
                </el-form-item>
                <el-form-item label="作业时长" hidden>
                    <el-input v-model="form.ht"></el-input>
                </el-form-item>
                <el-form-item label="总时长" hidden>
                    <el-input v-model="form.zsc"></el-input>
                </el-form-item>
                <el-form-item label="交接班">
                    <el-input v-model="form.jjb"></el-input>
                </el-form-item>
                <el-form-item label="开仓盖">
                    <el-input v-model="form.kcg"></el-input>
                </el-form-item>
                <el-form-item label="停工吃饭">
                    <el-input v-model="form.tgcf"></el-input>
                </el-form-item>
                <el-form-item label="超限箱">
                    <el-input v-model="form.cxx"></el-input>
                </el-form-item>
                <el-form-item label="进出转换">
                    <el-input v-model="form.jczh"></el-input>
                </el-form-item>
                <el-form-item label="完工时点" hidden>
                    <el-input v-model="form.wgsd"></el-input>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="saveEdit">确 定</el-button>
                <el-button @click="editVisible = false">取 消</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
import Axios from 'axios';
import { time } from 'echarts';
export default {
    name: 'baseform',
    data() {
        return {
            form: {
                name: '',
                count: '',
                inp: '',
                incount: '',
                outp: '',
                count: '',
                date: '',
                time: ''
            },
            edit_form: {
                name: '',
                count: '',
                inp: '',
                incount: '',
                outp: '',
                count: '',
                date: '',
                time: ''
            },
            tableData: [],
            multipleSelection: [],
            delList: [],
            editVisible: false,
            selectedId: '',
            shipdata: []
        };
    },
    created() {
        // this.getData();
        Axios.get(this.url.url + '/get_shipname').then((res) => {
            console.log(res);
            this.shipdata = res.data.list;
        });
    },
    methods: {
        onClear() {
            this.tableData = [];
        },
        selectchange() {
            let param = new URLSearchParams();
            param.append('id', this.selectedId);
            Axios({
                method: 'post',
                url: this.url.url + '/post_outsce_data',
                data: param
            }).then((res) => {
                console.log(res);
                this.tableData = res.data.res;
            });
        },
        onSub(id) {
            this.tableData[id].edit = false;
            var strtime = this.tableData[id].date + ' ' + this.tableData[id].time;
            var date = new Date(strtime.replace(/-/g, '/'));
            var time1 = date.getTime();
            // time2 = date.valueOf();
            // time3 = Date.parse(date);
            var all_t = parseInt(this.tableData[id].incount / this.tableData[id].inp + 2);
            time1 += all_t * 60 * 60 * 1000;
            var date1 = new Date(time1);
            var str_date1 =
                date1.getFullYear() +
                '-' +
                (date1.getMonth() + 1) +
                '-' +
                date1.getDate() +
                ' ' +
                date1.getHours() +
                ':' +
                date1.getMinutes() +
                ':' +
                date1.getSeconds();
            this.tableData[id].wgsd = str_date1;
            this.tableData[id].ht = this.tableData[id].incount / this.tableData[id].inp
        },
        onSubmit() {
            let param = new URLSearchParams();
            param.append('ship_id', this.selectedId);
            param.append('inp', this.form.inp);
            param.append('incount', this.form.incount);
            param.append('outp', this.form.outp);
            param.append('count', this.form.count);
            param.append('date', this.form.date);
            param.append('tabledata', JSON.stringify(this.tableData));
            Axios({
                method: 'post',
                url: this.url.url + '/set_outsch_data',
                data: param
            });
            this.$message.success('提交成功！');
        },
        onGenerate() {
            console.log(this.form.date);
            let ts = this.form.date.split(':');
            let count = this.form.count;
            for (var i = 0; i <= count; i++) {
                var strtime = this.form.date + ' ' + this.form.time;
                var date = new Date(strtime.replace(/-/g, '/'));
                var time1 = date.getTime();
                // time2 = date.valueOf();
                // time3 = Date.parse(date);
                var all_t = parseInt(this.form.incount / this.form.inp + 2);
                time1 += all_t * 60 * 60 * 1000;
                var date1 = new Date(time1);
                var str_date1 =
                    date1.getFullYear() +
                    '-' +
                    (date1.getMonth() + 1) +
                    '-' +
                    date1.getDate() +
                    ' ' +
                    date1.getHours() +
                    ':' +
                    date1.getMinutes() +
                    ':' +
                    date1.getSeconds();
                this.tableData.push({
                    edit: false,
                    id: i,
                    incount: this.form.incount,
                    inp: this.form.inp,
                    bw: i + 1,
                    ph: 40,
                    date: this.form.date,
                    time: this.form.time,
                    st: this.form.date + '  ' + this.form.time,
                    ht: this.form.incount / this.form.inp,
                    jjb: 20,
                    kcg: 20,
                    tgcf: 20,
                    cxx: 30,
                    jczh: 30,
                    zsc: this.form.incount / this.form.inp + 2,
                    wgsd: str_date1
                });
            }
        },
        // 删除操作
        handleDelete(index, row) {
            // 二次确认删除
            this.$confirm('确定要删除吗？', '提示', {
                type: 'warning'
            })
                .then(() => {
                    let del_id = this.tableData[index].id;
                    let param = new URLSearchParams();
                    param.append('del_id', del_id);
                    Axios({
                        method: 'post',
                        url: this.url.url + '/del_outsce_data',
                        data: param
                    });
                    this.$message.success('删除成功');
                    this.tableData.splice(index, 1);
                })
                .catch(() => {});
        },
        // 多选操作
        handleSelectionChange(val) {
            this.multipleSelection = val;
        },
        delAllSelection() {
            const length = this.multipleSelection.length;
            let str = '';
            this.delList = this.delList.concat(this.multipleSelection);
            for (let i = 0; i < length; i++) {
                str += this.multipleSelection[i].name + ' ';
            }
            this.$message.error(`删除了${str}`);
            this.multipleSelection = [];
        },
        // 编辑操作
        handleEdit(index, row) {
            this.idx = index;
            this.form = row;
            this.editVisible = true;
        },
        // 保存编辑
        saveEdit() {
            this.editVisible = false;
            this.$message.success(`修改第 ${this.idx + 1} 行成功`);
            // this.$set(this.tableData, this.idx, this.form);
            this.tableData[this.idx].bw = this.form.bw;
            this.tableData[this.idx].incount = this.form.incount;
            this.tableData[this.idx].ph = this.form.ph;
            this.tableData[this.idx].st = this.form.st;
            this.tableData[this.idx].jjb = this.form.jjb;
            this.tableData[this.idx].kcg = this.form.kcg;
            this.tableData[this.idx].tgcf = this.form.tgcf;
            this.tableData[this.idx].cxx = this.form.cxx;
            this.tableData[this.idx].jczh = this.form.jczh;
            this.tableData[this.idx].ht = this.form.incount / this.tableData[this.idx].inp;
            console.log(
                parseInt(this.tableData[this.idx].ht),
                parseInt(this.form.ph + this.form.jjb + this.form.kcg + this.form.tgcf + this.form.cxx + this.form.cxx) / 60
            );
            this.tableData[this.idx].zsc =
                parseInt(this.tableData[this.idx].ht) +
                (parseInt(this.form.ph) +
                    parseInt(this.form.jjb) +
                    parseInt(this.form.kcg) +
                    parseInt(this.form.tgcf) +
                    parseInt(this.form.cxx) +
                    parseInt(this.form.jczh)) /
                    60;
            var strtime = this.tableData[this.idx].date + ' ' + this.tableData[this.idx].time;
            var date = new Date(strtime.replace(/-/g, '/'));
            var time1 = date.getTime();
            // time2 = date.valueOf();
            // time3 = Date.parse(date);
            var all_t = this.tableData[this.idx].zsc
            time1 += all_t * 60 * 60 * 1000;
            var date1 = new Date(time1);
            var str_date1 =
                date1.getFullYear() +
                '-' +
                (date1.getMonth() + 1) +
                '-' +
                date1.getDate() +
                ' ' +
                date1.getHours() +
                ':' +
                date1.getMinutes() +
                ':' +
                date1.getSeconds();
            this.tableData[this.idx].wgsd = str_date1;
        }
    }
};
</script>

<style scoped>
.handle-box {
    margin-bottom: 20px;
}

.handle-select {
    width: 120px;
}

.handle-input {
    width: 300px;
    display: inline-block;
}
.table {
    width: 100%;
    font-size: 14px;
}
.red {
    color: #ff0000;
}
.mr10 {
    margin-right: 10px;
}
.table-td-thumb {
    display: block;
    margin: auto;
    width: 40px;
    height: 40px;
}
</style>
