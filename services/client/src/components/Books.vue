<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Let's Defeat Covid-19 !!</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-on:click="ask_shoudoku">消毒をお願いする</button>
        <h1>{{this.message}}</h1>
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
      message: '',
      showMessage: false,
      ROOT_API: "http://server:5000",
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    ask_shoudoku() {
      // # TODO ここをflaskとつなぎ込む
      // const path = `${this.ROOT_API}/info/ping`;
      axios.get(`http://server:5000/info/ping`)
        .then((res) => {
          this.message = res.data.message;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addBook(payload) {
      const path = `${this.ROOT_API}/books`;
      axios.post(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Book added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    updateBook(payload, bookID) {
      const path = `${this.ROOT_API}/books/${bookID}`;
      axios.put(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Book updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    removeBook(bookID) {
      const path = `${this.ROOT_API}/books/${bookID}`;
      axios.delete(path)
        .then(() => {
          this.getBooks();
          this.message = 'Book removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
  },
  created() {
    this.getBooks();
  },
};
</script>