<template lang="html">
  <div class="">
    <v-card tile raised>
      <v-card-title>
        {{ $t("text.searchBusRoute")}} :
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
              color="#DD137B"
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
              color="#006C4A"
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
              color="#F27D00"
              dark
              @click:close="chip4 = false"
            >
            {{$t('text.trolleys')}}
            </v-chip>

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
    } ,
    label () {
        return this.$t("text.search");
    } ,
    storedRoutes() {
        return this.$store.state.routes ;
    } ,
    storedStops() {
        return this.$store.state.stops ;
    } ,
    routes() {
        var ret = [] ;
        for (var route of this.storedRoutes) {
            ret.push({'text' : route.name , 'value' : {'id' : route.public_id , 'type': 'route'}})
        }
        return ret;
    } ,
    stops() {
        var ret = [] ;
        for (var stop of this.storedStops) {
            ret.push({'text' : stop.name , 'value' : {'id' : stop.public_id , 'type': 'stop'}})
        }
        return ret;
    } ,

  }
}
</script>

<style lang="css" scoped>
</style>
