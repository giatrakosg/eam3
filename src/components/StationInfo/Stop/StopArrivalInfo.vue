<template lang="html">
  <v-container fluid>
    <v-layout row>
      <v-flex sm1 md1 lg1>
        <v-spacer></v-spacer>
      </v-flex>
      <v-flex sm10 md10 lg10>
        <v-card color="secondary">
          <v-card-title> {{ this.id }}</v-card-title>
        </v-card>
      </v-flex>
      <v-flex sm1 md1 lg1>
        <v-spacer></v-spacer>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name : 'StopArrivalInfo' ,
  props : ['id']
}
</script>

<style lang="css" scoped>
</style>
