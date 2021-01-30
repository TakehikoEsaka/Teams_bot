<template>
  <div id="addschedule">
  </div>
</template>

<script>
export default {
  name: 'AddSchedule',
  data () {
      return {
          info: null,
          loading: true,
          errored: false,
          error: null,
      }
  },
  created () {
    axios.defaults.withCredentials = true
    axios
      .get(`/api/v4/projects/${this.project_id}/milestones`, {
        'params': {
          private_token: process.env.VUE_APP_GITLAB_PRIVATE_TOKEN,
          sort: "asc"
        }
      })
      .then(response => {
        (this.info = response.data)
      })
      .catch(err => {
        (this.errored = true), (this.error = err);
      })
      .finally(() => (this.loading = false))
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  margin: 0 10px;
}
a {
  color: #42b983;
}
#milestones {
  width: 100%;
}
</style>
