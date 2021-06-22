<template>
  <div class="row">
    <!-- Big Chart -->
    <div class="col-12">
      <card type="chart">
        <template slot="header">
        </template>
      </card>
    </div>

    <div class="col-lg-5">
      <card type="tasks" :header-classes="{ 'text-right': isRTL }">
        <template slot="header" class="d-inline">
          <h6 class="title d-inline">Задачи (5)</h6>
          <p class="card-category d-inline">Неделя</p>

          <base-dropdown
            menu-on-right=""
            tag="div"
            title-classes="btn btn-link btn-icon"
            class="float-right"
          >
            <i slot="title" class="tim-icons icon-settings-gear-63"></i>
            <a class="dropdown-item" href="#pablo"> Action </a>
            <a class="dropdown-item" href="#pablo"> Another action </a>
            <a class="dropdown-item" href="#pablo"> Something else </a>
          </base-dropdown>
        </template>
        <div class="table-full-width table-responsive">
          <task-list></task-list>
        </div>
      </card>
    </div>
    <div class="col-lg-7">
      <card card-body-classes="table-full-width">
        <h4 slot="header" class="card-title">Striped table</h4>
        <el-table data="">
          <el-table-column
            min-width="150"
            sortable
            label="Name"
            property="name"
          ></el-table-column>
          <el-table-column
            min-width="150"
            sortable
            label="Country"
            property="country"
          ></el-table-column>
          <el-table-column
            min-width="150"
            sortable
            label="City"
            property="city"
          ></el-table-column>
          <el-table-column
            min-width="150"
            sortable
            align="right"
            header-align="right"
            label="Salary"
            property="salary"
          ></el-table-column>
        </el-table>
      </card>
    </div>
  </div>
</template>
<script>
import LineChart from '@/components/Charts/LineChart';
import TaskList from '@/components/Dashboard/TaskList';
import { Table, TableColumn } from 'element-ui';


export default {
  name: 'dashboard',
  middleware: 'auth',
  components: {
    LineChart,
    TaskList,
    [Table.name]: Table,
    [TableColumn.name]: TableColumn
  },
  data () {
    return {
    };
  },
  computed: {
  },
  methods: {
    initBigChart (index) {

    }
  },
  mounted () {
    this.initBigChart(0);
  }
}
</script>
<style></style>
