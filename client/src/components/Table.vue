<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>WelbeX таблица</h1>
        <hr>

        <span>Фильтрация</span>
        <b-form-select v-model="selectedFilterColumn"
                       :options="filterFieldSelector"
                       size="sm"
                       class="mt-1"
        >
        </b-form-select>
        <b-form-select v-model="selectedFilterType"
                       :options="filterTypeSelector"
                       size="sm"
                       class="mt-1"
                       aria-placeholder="Выберите тип сортировки"
        >
        </b-form-select>
         <b-form-input size="sm" class="mt-1"
                       id="form-count-input"
                       type="text"
                       placeholder="Введите значение"
                       v-model="filterValue"
                       v-on:keyup.enter.native="sortOrder(selectedFilterColumn)"
         >
         </b-form-input>

        <br><br>

        <div class="overflow-auto">
          <table class="table table-hover">
            <thead>
            <tr>
              <th scope="col">Дата</th>
              <th @click="sortOrder('title')" scope="col">Название</th>
              <th @click="sortOrder('count')" scope="col">Количество</th>
              <th @click="sortOrder('distance')" scope="col">Расстояние</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(row, index) in rows" :key="index">
              <td>{{ row.date }}</td>
              <td>{{ row.title }}</td>
              <td>{{ row.count }}</td>
              <td>{{ row.distance }}</td>
            </tr>
            </tbody>
          </table>
        </div>
          <b-pagination v-model="currentPage"
                      :total-rows="this.total"
                      :per-page="perPage"
                      @input="sortOrder(null)"
                      align="center"
        ></b-pagination>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Notification from './Notification'; // Import notifications module for messages on page

export default {
  data() {
    return {
      perPage: 10, // Max count rows on page
      currentPage: 1, // Current page
      isDescOrder: true,
      rows: [], // Array rows from DB
      total: null,
      selectedFilterColumn: null, // Selected column for filter
      selectedFilterType: null, // Selected type for filter
      // Options for column selector
      filterFieldSelector: [
        { value: null, text: 'Выберите столбец для фильтрации' },
        { value: 'title', text: 'Название' },
        { value: 'count', text: 'Количество' },
        { value: 'distance', text: 'Расстояние' },
      ],
      // Options for type selector
      filterTypeSelector: [
        { value: null, text: 'Выберите тип фильтрации' },
        { value: 'equally', text: 'Равно' },
        { value: 'contains', text: 'Содержит' },
        { value: 'over', text: 'Больше' },
        { value: 'less', text: 'Меньше' },
      ],
      filterValue: '', // String for text of filter value
    };
  },
  components: {
    notification: Notification, // Notifications
  },
  computed: {
  },
  methods: {
    // Get all rows from back-end
    getRows(payload) {
      const path = 'http://localhost:5000/api/rows';
      axios.post(path, payload)
        .then((res) => {
          this.rows = res.data.rows;
          this.total = res.data.total;
        })
        .catch((error) => {
          /* eslint no-console: ["error", { allow: ["warn", "error"] }] */
          console.error(error);
        });
    },
    sortOrder(field) {
      const payload = {
        sortField: field,
        isDescOrder: this.isDescOrder,
        filterField: this.selectedFilterColumn,
        filterType: this.selectedFilterType,
        filterValue: this.filterValue,
        pageNo: this.currentPage,
        pageRowCount: this.perPage,
      };
      this.getRows(payload);
      this.isDescOrder = !this.isDescOrder;
      // eslint-disable-next-line
      console.log(this.rows.total);
    },
  },
  created() {
    this.getRows();
  },
};
</script>
