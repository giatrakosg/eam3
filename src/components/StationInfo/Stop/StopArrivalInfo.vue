<template lang="html">
  <v-container fluid>
    <v-layout row>
      <v-flex sm1 md1 lg1>
        <v-spacer></v-spacer>
      </v-flex>
      <v-flex sm10 md10 lg10>
        <v-card color="secondary">
          <v-card-title> Αφίξεις στις {{this.timestamp}}</v-card-title>
          <v-card-text>
            <template>
              <v-data-table raised tile
                :headers="headers"
                :items="route"
                :items-per-page="5"
                hide-default-footer
              ></v-data-table>
            </template>
          </v-card-text>
        </v-card>
      </v-flex>
      <v-flex sm1 md1 lg1>
        <v-spacer></v-spacer>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import moment from 'moment';

export default {
  name : 'StopArrivalInfo' ,
  props : ['id'] ,
  data () {
    return {
      arrivals : [
        {id : '136' , times : ['5mins','10mins']} ,
        {id : '137' , times : ['5mins','20mins']} ,
      ] ,
      headers : [
        { text: 'Δρομολογιο', value: 'id' },
        { text: 'Αφιξη', value: 'time' },

      ],
      timestamp : ''
    }
  } ,
  computed : {
    route () {
      var ret = []
      if (this.id == -1) {
        for (var i = 0; i < this.arrivals.length; i++) {
          for (var j = 0; j < this.arrivals[i].times.length; j++) {
            ret.push({id : this.arrivals[i].id , time : this.arrivals[i].times[j]})
          }
        }
      } else {
        var x = this.arrivals.find(route => route.id == this.id)
        for (var k = 0; k < x.times.length; k++) {
          ret.push({id : x.id , time : x.times[k]})
        }
      }
      return ret
    }
  } ,
  created() {
      setInterval(this.getNow, 1000);
  },
  methods : {
    getNow: function() {
        this.timestamp = moment().format('h:mm');
    }
  }

}
</script>

<style lang="css">
</style>
