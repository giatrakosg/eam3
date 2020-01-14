<template lang="html">
  <div class="">
      <!--
    <v-layout row wrap class="my-4">
      <v-flex sm1 md1 lg1>
        <v-spacer></v-spacer>
      </v-flex>
      <v-flex sm10 md10 lg10>
        <v-card raised tile>
          <v-card-title>
            {{ $t("text.buses")}}
            <v-icon>mdi-bus</v-icon>
          </v-card-title>
        </v-card>
      </v-flex>
      <v-flex xs1 sm1 md1 lg1>
        <v-spacer></v-spacer>
      </v-flex>
    </v-layout>
-->
    <v-layout row wrap>
      <v-flex x0 sm0 md1 lg1>
        <v-spacer></v-spacer>
      </v-flex>
      <v-flex sm2 md3 lg3>
        <div v-if="stopStatus && routesStatus">
          <SideBar />
        </div>
      </v-flex>
      <v-flex xs0 sm0 md1 lg1>
        <v-spacer></v-spacer>
      </v-flex>
      <v-flex xs10 sm10 md6 lg6>
        <MapSection />
      </v-flex>
      <v-flex sm0 md1 lg1>
        <v-spacer></v-spacer>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import MapSection from "../components/BusMaps/MapSection"
import SideBar from "../components/BusMaps/SideBar"

export default {
  name : 'BusMapsPage' ,
  components : {
    MapSection , SideBar
  } ,
  created () {
    this.$store.dispatch('getRoutes') ;
    this.$store.dispatch('getStops') ;

  } ,
  computed : {
    stopStatus() {
      return this.$store.state.stops_status == "success";
    } ,
    routesStatus() {
      return this.$store.state.routes_status === 'success';
    }
  }
}
</script>

<style lang="css" scoped>
</style>
