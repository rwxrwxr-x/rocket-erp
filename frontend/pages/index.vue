<template>
  <div class="row">
    <!-- Big Chart -->
    <active-customers></active-customers>
  </div>
</template>
<script>
import LineChart from '@/components/Charts/LineChart';
import TaskList from '@/components/Dashboard/TaskList';
import ActiveCustomers from "~/components/Customer/ActiveCustomers";
import { Table, TableColumn } from 'element-ui';


export default {
  name: 'dashboard',
  middleware: 'auth',
  components: {
    LineChart,
    TaskList,
    [Table.name]: Table,
    [TableColumn.name]: TableColumn,
    ActiveCustomers
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
