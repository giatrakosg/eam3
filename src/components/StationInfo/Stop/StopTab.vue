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
        <v-tab>
            <v-icon>
              mdi-bus
            </v-icon>
            136
        </v-tab>
        <v-tab>
            <v-icon>
              mdi-bus
            </v-icon>
            137
        </v-tab>
        <v-tab-item>
          <StopArrivalInfo :id="-1" />
        </v-tab-item>
        <v-tab-item>
          <StopArrivalInfo :id="136" />
        </v-tab-item>
        <v-tab-item>
          <StopArrivalInfo :id="137" />
        </v-tab-item>
      </v-tabs>
    </div>
</template>

<script>
import StopArrivalInfo from './StopArrivalInfo'
export default {
  components : {
    StopArrivalInfo
  }
}
</script>

<style lang="css" scoped>
</style>
