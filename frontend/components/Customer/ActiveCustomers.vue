<template>
   <div class="col-lg-5">
      <card card-body-classes="table-full-width">
        <h4 slot="header" class="card-title">Текущие заказчики</h4>
        <el-table :data="table_data"
        style="width: 100%;margin-bottom: 20px;"
        row-key="id"
        >
          <el-table-column type="expand">
            <template slot-scope="props">
              <div v-for="item in props.row.active_contracts">
                <p class="title">{{ item.name }}</p>
                  <nuxt-link class="card" :key="item.id" :to="'/customer/contracts/'+item.id">Перейти к договору</nuxt-link>
              </div>
            </template>
          </el-table-column>
          <el-table-column
            min-width="130"
            sortable
            label="Заказчик"
            property="name"
          ></el-table-column>
          <el-table-column
            min-width="100"
            sortable
            label="ИНН"
            property="inn">
          </el-table-column>
          <el-table-column
            min-width="70"
            sortable
            align="right"
            header-align="right"
            label="Активные"
            property="summary"
          ></el-table-column>
        </el-table>
      </card>
    </div>
</template>
<script>
import TaskList from '@/components/Customer/TaskList';
import { Table, TableColumn } from 'element-ui';

export default {
  middleware: 'auth',
  name: 'user',

  components: {
    TaskList,
    [Table.name]: Table,
    [TableColumn.name]: TableColumn
  },
  data: () => {
    return {
      table_data: [
          {
            id: "1",
            name: "name",
            active_contracts: [{
              id: "1",
              name: "con"
            }]
          },
                 {
            id: "1",
            name: "name",
            active_contracts: [{
              id: "1",
              name: "con"
            }]
          },
        ],
    }
  },
  created () {
    this.getData()
  },
  methods: {
    async getData() {
      await this.$store.dispatch('customers/active_customers')
      const temp = {...this.$store.getters["customers/active_customers"]}
      let response = Object.values(temp)
      for (let i = 0; i < response.length; i++) {
        response[i].summary = response[i]['active_contracts'].length
      }
      this.table_data = response
    }
  }
};


</script>
<style></style>
