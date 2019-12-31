<template lang="html">
  <div class="">
    <v-layout row wrap class="my-4">
      <v-flex sm1 md1 lg1>
        <v-spacer></v-spacer>
      </v-flex>
      <v-flex sm10 md10 lg10>
        <v-card raised tile>
          <v-card-title>
            Λεωφορεία
            <v-icon>mdi-bus</v-icon>
          </v-card-title>
        </v-card>
      </v-flex>
      <v-flex sm1 md1 lg1>
        <v-spacer></v-spacer>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex sm1 md1 lg1>
        <v-spacer></v-spacer>
      </v-flex>
      <v-flex sm3 md3 lg3>
        <SideBar />
      </v-flex>
      <v-flex sm1 md1 lg1>
        <v-spacer></v-spacer>
      </v-flex>
      <v-flex sm6 md6 lg6>
        <MapSection />
      </v-flex>
      <v-flex sm1 md1 lg1>
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
  }
}
</script>

<style lang="css" scoped>
</style>
