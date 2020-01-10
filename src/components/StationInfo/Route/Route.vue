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
                  <v-list-item-title class="headline mb-1">{{route.name}}</v-list-item-title>
                  <v-list-item-subtitle>Απο : {{from.name}}</v-list-item-subtitle>
                  <v-list-item-subtitle>Προς : {{to.name}}</v-list-item-subtitle>
                </v-list-item-content>

                <v-list-item-avatar
                  raised
                  size="80"
                  color="primary"
                >{{route.name}}</v-list-item-avatar>
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
                  <th class="text-left">Προσβαση</th>
                </tr>
              </thead>
              <tbody>

                <tr v-for="item in stations" :key="item.name">
                  <td>{{ item.name }}</td>
                  <td class="align-left">
                      <v-btn
                      :to="'/stop/' + item.public_id"
                      color="primary"
                      tile
                      raised
                      >
                          <v-icon>mdi-arrow-right-bold</v-icon>
                      </v-btn>
                  </td>
                      <td v-if="item.accesible">
                          <v-icon>
                              mdi-wheelchair-accessibility
                          </v-icon>
                      </td>
                      <td v-if="item.accesible == false">
                          <v-icon>
                              mdi-car-brake-alert
                          </v-icon>
                      </td>
                </tr>

              </tbody>
            </template>
          </v-simple-table>
        </v-flex>
        <v-flex xs1 sm1 md1></v-flex>
        <v-flex xs6 sm6 md6 align-left >
          <l-map :zoom="zoom" :center="center" style="z-index: 0; height: 50vh; width: 100%"
          >
            <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
            <l-marker
                v-for="marker in positions"
                :key="marker.id"
                :lat-lng="marker.position">
                <l-popup>
                    {{marker.name}}
                </l-popup>
            </l-marker>
            <l-polyline
              :lat-lngs="positions.map(a => a.position)"
            >
            </l-polyline>
          </l-map>
        </v-flex>

      </v-layout>
    </v-container>
  </div>
</template>

<script>
import {LMap, LTileLayer, LMarker,LPolyline, LPopup  } from 'vue2-leaflet';
import L from 'leaflet'

export default {
  name : 'Route' ,
  props : ['id'] ,
  data() {
    return {
       zoom:13,
       url: 'http://mt.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
       markers : [
         {id : 0 ,lat : 37.933163 , lng: 23.714648 },
         {id : 1 ,lat : 37.938451 , lng: 23.721009 },
         {id : 2 ,lat : 37.943653 , lng: 23.727682 },
       ]

    }
  } ,
  components: {
    LMap ,
    LTileLayer,
    LMarker ,
    LPolyline ,
    LPopup
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
  computed : {
      /*
    points () {
      let route = this.routes[0];
      let positions = [];
      for (var i = 0; i < route.stations.length; i++) {
        positions.push({ id : route.stations[i].id , position : route.stations[i].position });
      }
      return positions ;
    },
    */


    // We need the following data to display
    // 1. Name
    // 2. Direction
    // 3. First Stop name
    // 4. Last stop name
    // 5. List of stops with
    // 5.1 Name
    // 5.2 public id
    // 5.3 position
    route () {
        return this.$store.state.route ;
    } ,
    stations() {
        var stationsL = [] ;
        var stations_list = this.$store.state.route.stations ;
        for (let station of stations_list) {
            stationsL.push(station.stop);
        }
        return stationsL ;
    } ,
    positions () {
      let positions = [];
      for (var i = 0; i < this.stations.length; i++) {
          let id = i ;
          let name = this.stations[i].name ;
          let lat = this.stations[i].lat ;
          let lng = this.stations[i].lng ;
          positions.push({"id" : id , "position" : L.latLng(lat,lng) , "name" : name} );
      }
      return positions ;

    } ,
    // We calculate the center point by averaging each coordinate
    center() {
        let sumx = 0 ;
        let sumy = 0 ;
        for (let point of this.positions) {
            sumx += point.position.lat ;
            sumy += point.position.lng ;
        }
        let len = this.positions.length ;
        return L.latLng(sumx / len , sumy / len);
    } ,
    from() {
        let s ;
        for (let station of this.stations) {
            if (station.public_id == this.route.first_stop) {
                s = station ;
                break ;
            }
        }
        return s ;
    } ,
    to() {
        let s ;
        for (let station of this.stations) {
            if (station.public_id == this.route.last_stop) {
                s = station ;
                break ;
            }
        }
        return s ;
    }

  }

}
</script>


<style scoped>
</style>
