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
      <v-flex sm5 md5 lg5>
        <v-card>
          <v-card-text>hello</v-card-text>
        </v-card>
      </v-flex>
      <v-flex sm1 md1 lg1>
        <v-spacer></v-spacer>
      </v-flex>
      <v-flex sm4 md4 lg4>
        <v-card>
          <v-card-text>hello</v-card-text>
        </v-card>
      </v-flex>
      <v-flex sm1 md1 lg1>
        <v-spacer></v-spacer>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
export default {
  name : 'BusMapsPage'
}
</script>

<style lang="css" scoped>
</style>
