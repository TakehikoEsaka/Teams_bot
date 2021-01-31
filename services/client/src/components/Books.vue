<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Let's Defeat Covid-19 !!</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        
        <button type="button" class="btn btn-success btn-sm" v-on:click="confirm_status">今日のステータスを確認する</button>
        <h1>{{this.message_confirm_status}}</h1>
        
        <button type="button" class="btn btn-success btn-sm" v-on:click="ask_shoudoku">消毒をお願いする</button>
        <h1>{{this.message_ask_shoudoku}}</h1>
        <br><br>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert';
export default {
  data() {
    return {
      books: [],
      addSchedule: {
        title: '',
        author: '',
        read: [],
      },
      editForm: {
        id: '',
        title: '',
        author: '',
        read: [],
      },
      message_ask_shoudoku: '',
      message_confirm_status: '',
      showMessage: false,
      ROOT_API: "http://server:5000",
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    set_value() {
      this.message_ask_shoudoku = ""
      this.message_confirm_status = ""
    },
    ask_shoudoku() {
      // const path = `${this.ROOT_API}/info/ping`;
      axios.get(`http://localhost:5011/ask_shoudoku`)
        .then((res) => {
          this.message_ask_shoudoku = res.data.message;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    confirm_status() {
      axios.get(`http://localhost:5011/confirm_status`)
        .then((res) => {
          this.message_confirm_status = res.data.message;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  created() {
    this.set_value();
  },
  }
}
</script>