<template lang="html">
  <div class="">
    <v-card tile raised>
      <v-card-title>
        {{ $t("text.searchBusRoute")}} :
      </v-card-title>
      <v-card-text>
        <div>
          <v-autocomplete
            v-model="selected"
            :label="this.label"
            :items="components"
            item-color="primary"
          ></v-autocomplete>
          <div v-if="selected">
            <div v-if="selected.type == 'route'">
              Route : <RouteInfoCard :id="selected.id" />
            </div>
            <div v-if="selected.type == 'stop'">
              Stop :  <StopInfoCard :id="selected.id" />
            </div>
          </div>
        </div>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import RouteInfoCard from '../StationInfo/Route/RouteInfoCard'
import StopInfoCard from '../StationInfo/Stop/StopInfoCard'
export default {
  name : 'SideBar' ,
  data() {
    return {
      routes: [
        { text : '136 προς Νεο Κοσμο' , value : { id : 0 , type : 'route'}},
        { text : '136 προς Φαληρο'    , value : { id : 1 , type : 'route'} },
        { text : '218 προς Πειραια'   , value : { id : 2 , type : 'route'} },
        { text : '218 προς Καλιθέα'   , value : { id : 3 , type : 'route'} },
      ],
      stops : [
        { text : '3η Αιγαιου'  , value : { id : 4 , type : 'stop'} },
        { text : '10η Αιγαιου' , value : { id : 5 , type : 'stop'} },
        { text : 'Νεκροταφεία' , value : { id : 6 , type : 'stop'} },
      ] ,
      selected : ''
    }
  } ,
  components : {
    RouteInfoCard ,
    StopInfoCard ,
  },
  computed : {
    components() {
      return this.routes.concat(this.stops) ;
    } ,
    label () {
        return this.$t("text.search");
    }
  }
}
</script>

<style lang="css" scoped>
</style>
