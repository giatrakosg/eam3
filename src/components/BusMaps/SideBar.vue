<template lang="html">
  <div class="">
    <v-card tile raised>
      <v-card-title>
        Αναζήτηση Στάσης ή Γραμμής:
      </v-card-title>
      <v-card-text>
            <v-btn
              v-if="!chip1 && !chip2 && !chip3 && !chip4"
              close
              color="primary"
              dark
              @click="chip1 = true, chip2 = true, chip3 = true, chip4= true"
            >
            {{$t('text.reset')}}
            </v-btn>

            <v-chip
              v-if="chip1"
              close
              color="primary"
              dark
              @click:close="chip1 = false"
            >
            {{$t('text.buses')}}
            </v-chip>

            <v-chip
              v-if="chip2"
              close
              color="green"
              text-color="white"
              dark
              @click:close="chip2 = false"
            >
            {{$t('text.tram')}}
            </v-chip>

            <v-chip
              v-if="chip3"
              class="ma-2"
              close
              color="red"
              dark
              text-color="white"
              @click:close="chip3 = false"
            >
              {{$t('text.metro')}}
            </v-chip>

            <v-chip
              v-if="chip4"
              class="ma-2"
              close
              color="orange"
              dark
              @click:close="chip4 = false"
            >
            {{$t('text.trolleys')}}
            </v-chip>

          <v-autocomplete
            v-model="selected"
            label="Αναζητηση"
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
      selected : '' ,
      chip1: true,
      chip2: true,
      chip3: true,
      chip4: true,
    }
  } ,
  components : {
    RouteInfoCard ,
    StopInfoCard ,
  },
  computed : {
    components() {
      return this.routes.concat(this.stops) ;
    }
  }
}
</script>

<style lang="css" scoped>
</style>
