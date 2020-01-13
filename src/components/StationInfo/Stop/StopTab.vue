<template lang="html">
    <div class="">
      <v-tabs
        v-model="tab"
        background-color="primary"
        class="elevation-2"
        dark
      >
        <v-tab>
            Όλες οι γραμμες
        </v-tab>
        <v-tab v-for="route in routes" :key="route">
            <v-icon>
              mdi-bus
            </v-icon>
            {{route.name}}
        </v-tab>
        <v-tab-item>
          <StopArrivalInfo :id="-1" />
        </v-tab-item>
        <v-tab-item v-for="route in routes" :key="route">
            <StopArrivalInfo :id="route" />
        </v-tab-item>
      </v-tabs>
    </div>
</template>

<script>
import StopArrivalInfo from './StopArrivalInfo'
export default {
  components : {
    StopArrivalInfo
  } ,
  computed : {
      stop() {
          return this.$store.state.stop ;
      } ,
      routes() {
          return this.stop.routes ;
      }
  }
}
</script>

<style lang="css" scoped>
</style>
