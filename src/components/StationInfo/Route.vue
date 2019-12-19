<template lang="html">
  <div >
    <v-container>
        <v-layout row class="my-4">
            <v-flex xs1 sm1 md1 >
              <v-card flat color="primary" height="100%" tile>
              <v-card-title class=" white--white" >{{routes[0].number}}</v-card-title>
              </v-card>
            </v-flex>
            <v-flex xs11 sm11 md11 >
              <v-card  color="white" tile raised>
              <v-card-title class=" white--white" >{{routes[0].direction}}</v-card-title>
              </v-card>
            </v-flex>
        </v-layout>
        <v-layout row class="my-4" >
          <v-flex xs1 sm1 md1 >
            <v-spacer></v-spacer>
          </v-flex>
          <v-flex xs3 sm3 md3 >
            <v-card  color="white" tile>
            <v-card-title class=" white--white" >Απο: {{routes[0].from}}</v-card-title>
            </v-card>
          </v-flex>
          <v-flex xs3 sm3 md3 >
            <v-card  color="white" tile>
            <v-card-title class=" white--white" >Προς : {{routes[0].to}}</v-card-title>
            </v-card>
          </v-flex>
          <v-flex xs4 sm4 md4 >
            <v-card  color="white" tile>
            <v-card-title class=" white--white" >Show map</v-card-title>
            </v-card>
          </v-flex>
      </v-layout>
      <v-layout row
      >
        <v-flex xs1 sm1 md1 >
          <v-spacer></v-spacer>
        </v-flex>
        <v-flex xs10 sm10 md10 >
          <v-data-table
            :headers="headers"
            :items="routes[0].stations"
            :items-per-page="5"
            class="elevation-1"
            hide-default-header
            hide-default-footer
          >
          <template v-slot:item.id="{ id }">
            <v-chip :color="primary" dark>{{ item.id }}</v-chip>
          </template>

          </v-data-table>
        </v-flex>

      </v-layout>
        <v-layout row>
          <v-flex xs1 sm1 md1 >
            <v-spacer></v-spacer>
          </v-flex>

          <v-flex xs10 sm10 md10 align-left >
            <v-timeline>
              <v-timeline-item v-for="item in routes[0].stations" :key="item.id" class="text-right" right>
                <v-card>
                  <v-card-title>{{item.name}}</v-card-title>
                </v-card>
              </v-timeline-item>
            </v-timeline>
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
      routes : [{id:2,number:136,direction:'Προς Στ. Φιξ',from:'Νεα Σμυρνη' ,to : 'Φιξ' ,
      stations : [{id : 0 , name : 'Ευαγγελικη'},{id : 1 , name : 'Αιγαιου 1'},{id : 2 , name : 'Αιγαιου 3'},{id : 3 , name : 'Εφεσου'},{id : 4 , name : 'Παντειος'},{id : 5 , name : 'Φιξ'}]}] ,
      stations : [{id : 0 , name : 'ev'},{id : 1 , name : 'ag 1'},{id : 2 , name : 'ag 3'},{id : 3 , name : 'ef'},{id : 4 , name : 'pa'},{id : 5 , name : 'f'}] ,
      headers :
        [
          {text : 'id' , value : 'id'},
          {text : 'name' , value : 'name'},

        ]
       ,
    }
  } ,
  components: {
  }

}
</script>

<style>
.v-timeline-item__divider {
  min-width: 64px;
}
.v-timeline--dense .v-timeline-item__body {
  max-width: calc(100% - 64px);
}
.v-application--is-ltr .v-timeline--dense:not(.v-timeline--reverse):before {
    left: 0px
}
</style>
