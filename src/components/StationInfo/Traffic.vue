<template lang="html">
  <div class="">
    <v-card>
      <v-card-title style="background:#1565C0 ">
        <span style="color: aliceblue">
          <v-icon> mdi-refresh </v-icon>
          Πληροφορίες Κίνησης στις  {{this.timestamp}}
        </span>
      </v-card-title>
      <v-layout row wrap>
        <v-flex sm2 md2 lg2>
          <v-card-text>
              <v-img
                height="40"
                width="40"
                src="../../assets/green_logo.jpg">
              </v-img>
          </v-card-text>
        </v-flex>
        <v-flex sm10 md10 lg10>
          <v-card-text>
            <v-chip
            color="success"
            >
              1
            </v-chip>
            <v-chip
            color="orange"
            >
              2
            </v-chip>
            <v-chip
            color="success"
            >
              3
            </v-chip>
          </v-card-text>
        </v-flex>
      </v-layout>
      <v-layout row>
        <v-flex sm2 md2 lg2>
          <v-card-text>
              <v-img
              height="40"
              width="40"
                src="../../assets/indigo_logo.jpg">
              </v-img>
          </v-card-text>
        </v-flex>
        <v-flex sm10 md10 lg10>
          <v-card-text>
            <v-chip
            color="success"
            >
              1
            </v-chip>
            <v-chip
            color="red"
            >
              2
            </v-chip>
            <v-chip
            color="success"
            >
              3
            </v-chip>
          </v-card-text>
        </v-flex>
      </v-layout>
      <v-layout row>
        <v-flex sm2 md2 lg2>
          <v-card-text>
              <v-img
              height="40"
              width="40"
                src="../../assets/orange_logo.jpg">
              </v-img>
          </v-card-text>
        </v-flex>
        <v-flex sm10 md10 lg10>
          <v-card-text>
            <v-chip v-model="value" filter color="success">Καμια διακοπη</v-chip>
          </v-card-text>
        </v-flex>
      </v-layout>
      <v-layout row>
        <v-flex sm2 md2 lg2>
          <v-card-text>
              <v-img
              height="40"
              width="40"
                src="../../assets/blue_logo.jpg">
              </v-img>
          </v-card-text>
        </v-flex>
        <v-flex sm10 md10 lg10>
          <v-card-text>
            <v-chip v-model="value" filter color="success">Καμια διακοπη</v-chip>
          </v-card-text>
        </v-flex>
      </v-layout>

    </v-card>
  </div>
</template>

<script>
import moment from 'moment';
export default {
  name : 'Traffic' ,
  data () {
    return {
      timestamp : '' ,
      value : true
    }
  },
  created() {
      setInterval(this.getNow, 1000);
  },
  methods: {
      getNow: function() {
          this.timestamp = moment().format('h:mm');
      }
  }

}
</script>

<style lang="css" scoped>
</style>
