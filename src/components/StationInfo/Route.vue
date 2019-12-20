<template lang="html">
  <div >
    <v-container>
        <v-layout row class="my-4" wrap>
          <v-flex xs12 sm12 md12 >
            <v-card
              class="mx-auto"
              outlined raised
            >
              <v-list-item three-line>
                <v-list-item-content>
                  <v-list-item-title class="headline mb-1">{{routes[0].direction}}</v-list-item-title>
                  <v-list-item-subtitle>Απο : {{routes[0].from}}</v-list-item-subtitle>
                  <v-list-item-subtitle>Προς : {{routes[0].to}}</v-list-item-subtitle>
                </v-list-item-content>

                <v-list-item-avatar
                  raised
                  size="80"
                  color="primary"
                >136</v-list-item-avatar>
              </v-list-item>
            </v-card>
          </v-flex>
        </v-layout>
        <v-layout row class="my-4" >
          <v-flex xs1 sm1 md1 >
            <v-spacer></v-spacer>
          </v-flex>
      </v-layout>
      <v-layout row
      >
        <v-flex xs1 sm1 md1 >
          <v-spacer></v-spacer>
        </v-flex>
        <v-flex xs10 sm10 md10 >
        </v-flex>

      </v-layout>
      <v-layout row>
        <v-flex xs5 sm5 md5 >
          <v-simple-table raised>
            <template v-slot:default>
              <thead>
                <tr>
                  <th class="text-left">Ονομα Στασης</th>
                  <th class="text-left">Πληροφοριες</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in routes[0].stations" :key="item.name">
                  <td>{{ item.name }}</td>
                  <td class="align-left"> <i class="fa fa-info-circle"></i>
                  </td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-flex>
        <v-flex xs1 sm1 md1></v-flex>
        <v-flex xs6 sm6 md6 align-left >
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
