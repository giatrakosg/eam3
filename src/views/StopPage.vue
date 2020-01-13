<template>
  <div>
    <v-layout row class="my-4">
      <v-flex sm1 md1 lg1>
        <v-spacer></v-spacer>
      </v-flex>
      <v-flex sm10 md10 lg10>
        <v-card>
            <v-card-title >{{stop.name}}</v-card-title>
            <v-card-text class="ma-0 pa-0">
              <!-- <StopTab /> -->
            </v-card-text>
        </v-card>
      </v-flex>
      <v-flex sm1 md1 lg1>
        <v-spacer></v-spacer>
      </v-flex>
    </v-layout>
    <v-layout row>
      <v-flex sm1 md1 lg1>
        <v-spacer></v-spacer>
      </v-flex>
      <v-flex sm10 md10 lg10>
        <StopTab />
      </v-flex>
      <v-flex sm1 md1 lg1>
        <v-spacer></v-spacer>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import StopTab from "../components/StationInfo/Stop/StopTab"
  export default {
    name : 'StopPage' ,
    props : ['id'] ,
    components : {
      StopTab
    } ,
    created () {
        this.$store.dispatch('getSelectedStop',this.id);
    } ,
    computed : {
        stop() {
            return this.$store.state.stop ;
        }
    }
  }
</script>
<style lang="css" scoped>
</style>
