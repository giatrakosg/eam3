<template lang="html">
    <div class="">
      <v-tabs
        v-model="tab"
        background-color="primary"
        class="elevation-2"
        dark
        :centered="centered"
        :grow="grow"
        :vertical="vertical"
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
          <StopArrivalInfo :id="100" />
        </v-tab-item>
        <v-tab-item>
          Lorem ipsum dolor
        </v-tab-item>
        <v-tab-item>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
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
