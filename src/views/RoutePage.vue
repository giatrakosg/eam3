<template lang="html">
  <div class="">
    <Route id="1" />
  </div>
</template>

<script>
import Route from "../components/StationInfo/Route/Route"
export default {
  name : 'RoutePage' ,
  props : ['id'] ,
  components : {
    Route
  } ,
  created() {
    this.$store.dispatch('getSelectedRoute',this.id);
  }
}
</script>

<style lang="css" scoped>
</style>
