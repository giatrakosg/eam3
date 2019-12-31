<template lang="html">
  <div >
    <v-container>
      <v-layout row>
        <v-flex xs12 sm12 md12 >
          <l-map :zoom="zoom" :center="center"
          style="z-index: 0; height: 50vh; width: 100"
          >
            <l-tile-layer :url="url" ></l-tile-layer>
            <l-marker v-for="marker in markers" :key="marker.id" :lat-lng="marker.position">
              <l-popup>
                {{marker.name}}
                <div v-for="line in marker.routesThrough" :key="line">
                  {{line}}
                </div>
              </l-popup>
            </l-marker>
          </l-map>
        </v-flex>

      </v-layout>
    </v-container>
  </div>
</template>

<script>
import {LMap, LTileLayer, LMarker , LPopup} from 'vue2-leaflet';
import L from 'leaflet'

export default {
  name : 'MapSection' ,
  props : ['id'] ,
  data() {
    return {
       zoom:14,
       center: L.latLng(37.938451, 23.721009),
       url: 'http://mt.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
       markers : [
         {id : 0 , position : L.latLng(37.933163,23.714648) , name : 'Ευαγγελική' , routesThrough : ['136,218']},
         {id : 1 , position : L.latLng(37.938451,23.721009) , name : 'Νεκτροταφεια' , routesThrough : ['136,137']},
         {id : 2 , position : L.latLng(37.943653,23.727682) , name : 'Δαφνη' , routesThrough : ['136']},
       ]

    }
  } ,
  components: {
    LMap ,
    LTileLayer,
    LMarker ,
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
  mounted() {
      this.$nextTick(() => {
        this.$refs.myMap.mapObject.ANY_LEAFLET_MAP_METHOD();
      })
  } ,
  computed : {
    points () {
      let route = this.routes[0];
      let positions = [];
      for (var i = 0; i < route.stations.length; i++) {
        positions.push({ id : route.stations[i].id , position : route.stations[i].position });
      }
      return positions ;
    },
    positions () {
      let route = this.routes[0];
      let positions = [];
      for (var i = 0; i < route.stations.length; i++) {
        positions.push(route.stations[i].position );
      }
      return positions ;

    }
  }

}
</script>


<style lang="css" scoped>
</style>
