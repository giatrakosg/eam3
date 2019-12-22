<template lang="html">
  <div class="">
    <v-card>

      <v-card-title>Πληροφορίες Κίνησης στις  {{this.timestamp}}</v-card-title>
    </v-card>
  </div>
</template>

<script>
import moment from 'moment';
export default {
  name : 'Traffic' ,
  data () {
    return {
      timestamp : ''
    }
  },
  created() {
      setInterval(this.getNow, 1000);
  },
  methods: {
      getNow: function() {
          this.timestamp = moment().format('h:mm');
      }
  }

}
</script>

<style lang="css" scoped>
</style>
