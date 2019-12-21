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
        <v-flex xs5 sm5 md5 align-left >
          <v-simple-table>
            <template v-slot:default>
              <thead>
                <tr>
                  <th class="text-left">Name</th>
                  <th class="text-left">Calories</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in routes[0].stations" :key="item.name">
                  <td>{{ item.name }}</td>
                  <td>keno</td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-flex>
        <v-flex xs7 sm7 md7 align-left >
          <l-map :zoom="zoom" :center="center"
          >
            <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
            <l-marker :lat-lng="marker"></l-marker>
          </l-map>
        </v-flex>

      </v-layout>

    </v-container>
  </div>
</template>

<script>
import {LMap, LTileLayer, LMarker } from 'vue2-leaflet';
import L from 'leaflet'

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
       zoom:13,
       center: L.latLng(47.413220, -1.219482),
       url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
       attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
       marker: L.latLng(47.413220, -1.219482),

    }
  } ,
  components: {
    LMap ,
    LTileLayer, LMarker
  } ,
  methods : {
    zoomUpdated (zoom) {
        this.zoom = zoom;
    },
    centerUpdated (center) {
        this.center = center;
    },
    boundsUpdated (bounds) {
        this.bounds = bounds;
    } ,
    removeMarker(index) {
        this.markers.splice(index, 1);
    },
    addMarker(event) {
        this.markers.push(event.latlng);
    } ,
  } ,
  mounted() {
      this.$nextTick(() => {
        this.$refs.myMap.mapObject.ANY_LEAFLET_MAP_METHOD();
      })
  }

}
</script>

<style scoped>
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
