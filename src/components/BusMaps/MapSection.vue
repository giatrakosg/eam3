<template lang="html">
  <div >
    <v-container>
      <v-layout row>
        <v-flex xs1 sm1 md1></v-flex>
        <v-flex xs10 sm10 md10 >
          <div class="map">
            <l-map :zoom="zoom" :center="center"
            style="z-index: 0; height: 50vh; width: 100"
            >
              <l-tile-layer :url="url" ></l-tile-layer>
              <l-marker v-for="marker in points" :key="marker.id" :lat-lng="marker.position"></l-marker>
              <l-polyline
                :lat-lngs="positions"
              >
              </l-polyline>
            </l-map>
          </div>
        </v-flex>

      </v-layout>
    </v-container>
  </div>
</template>

<script>
import {LMap, LTileLayer, LMarker , LPolyline } from 'vue2-leaflet';
import L from 'leaflet'

export default {
  name : 'MapSection' ,
  props : ['id'] ,
  data() {
    return {
      routes : [
        {
          id:2,
          number:136,
          direction:'Προς Στ. Φιξ',
          from:'Νεα Σμυρνη' ,
          to : 'Φιξ' ,
          stations :
            [
              {id : 0 , name : 'Ευαγγελικη' , position :  L.latLng(37.933163, 23.714648)},
              {id : 1 , name : 'Αιγαιου 1' , position :  L.latLng(37.938451, 23.721009)},
              {id : 2 , name : 'Αιγαιου 3' , position :  L.latLng(37.943653, 23.727682)},
              {id : 3 , name : 'Εφεσου' , position :  L.latLng(37.938451, 23.721009)},
              {id : 4 , name : 'Παντειος' , position :  L.latLng(37.938451, 23.721009)},
              {id : 5 , name : 'Φιξ' , position :  L.latLng(37.938451, 23.721009)}

            ]} ,
        {
          id:3,
          number:136,
          direction:'Προς Συνταγμα',
          from:'Νεο Κοσμο' ,
          to : 'Φιξ' ,
          stations :
          [
            {id : 0 , name : 'Ευαγγελικη'},
            {id : 1 , name : 'Αιγαιου 1'},
            {id : 2 , name : 'Αιγαιου 3'},
            {id : 3 , name : 'Εφεσου'},
            {id : 4 , name : 'Παντειος'},
            {id : 5 , name : 'Φιξ'}
          ]}
      ] ,


      stations : [
        {id : 0 , name : 'ev'},
        {id : 1 , name : 'ag 1'},
        {id : 2 , name : 'ag 3'},
        {id : 3 , name : 'ef'},
        {id : 4 , name : 'pa'},
        {id : 5 , name : 'f'} ,
      ] ,
      headers :
        [
          {text : 'id' , value : 'id'},
          {text : 'name' , value : 'name'},

        ]
       ,
       zoom:13,
       center: L.latLng(37.938451, 23.721009),
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
    LPolyline
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


<style lang="css" scoed>
.foobar1 {
  width: 100%;
  height: 400px;
}
</style>
