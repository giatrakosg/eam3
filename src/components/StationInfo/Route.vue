<template lang="html">
  <div >
    <v-container>
        <v-layout row wrap>
          <v-flex xs1 sm1 md1 >
            <v-card flat color="primary">
            <v-card-title class="justify-center white--white" >{{routes[0].number}}</v-card-title>
            </v-card>
          </v-flex>
          <v-flex xs11 sm11 md11 >
            <v-card  color="white">
            <v-card-title class="justify-center white--white" >{{routes[0].direction}}</v-card-title>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
  </div>
</template>

<script>
export default {
  name : 'Route' ,
  props : ['id'] ,
  data() {
    return {
      routes : [{id:2,number:136,direction:'Προς Στ. Φιξ'}]
    }
  }
}
</script>

<style lang="css" scoped>
</style>
