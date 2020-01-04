<template lang="html">
  <div >
    <v-container>
        <v-layout row class="my-4" wrap>
          <v-flex xs12 sm12 md12 >
            <v-card
              class="mx-auto"
              outlined raised
            >
              <v-list-item three-line>
                <v-list-item-content>
                  <v-list-item-title class="headline mb-1">{{stop.name}}</v-list-item-title>
                  <v-list-item-subtitle>Διερχομενες Γραμμες : </v-list-item-subtitle>
                  <div v-for="r in route" :key="r.id">
                    <v-list-item-subtitle>
                      {{r.number}} {{r.direction}}
                      <v-btn :to="'/bus/route/' + r.id" color="primary">
                        <v-icon> mdi-arrow-right-bold </v-icon>
                      </v-btn>
                    </v-list-item-subtitle>
                  </div>

                </v-list-item-content>
              </v-list-item>
            </v-card>
          </v-flex>
        </v-layout>
        <v-layout row class="my-4" >
          <v-flex xs1 sm1 md1 >
            <v-spacer></v-spacer>
          </v-flex>
      </v-layout>
      <v-layout row>
        <v-flex sm12 md12 lg12>
          <v-btn
          :to="'/stop/' + this.id"
          color="success"
          block
          raised
          tile
          >
            Περισσοτερες Πληροφοριες
          </v-btn>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>

export default {
  name : 'StopInfoCard' ,
  props : ['id'] ,
  data() {
    return {
      stops : [
        { name : '3η Αιγαιου'  , id : 4 },
        { name : '10η Αιγαιου' , id : 5 },
        { name : 'Νεκροταφεία' , id : 6 },
      ] ,
      routes : [
        {
          id:2,
          idStop : 4 ,
          number:136,
          direction:'Προς Στ. Φιξ',
          from:'Νεα Σμυρνη' ,
          to : 'Φιξ' ,
        },
        {
          id:3,
          idStop : 4 ,
          number:136,
          direction:'Προς Συνταγμα',
          from:'Νεο Κοσμο' ,
          to : 'Φιξ' ,
        } ,
        {
          id:3,
          idStop : 5 ,
          number:136,
          direction:'Προς Συνταγμα',
          from:'Νεο Κοσμο' ,
          to : 'Φιξ' ,
        } ,
        {
          id:3,
          idStop : 5 ,
          number:136,
          direction:'Προς Συνταγμα',
          from:'Νεο Κοσμο' ,
          to : 'Φιξ' ,
        } ,
        {
          id:3,
          idStop : 6 ,
          number:136,
          direction:'Προς Συνταγμα',
          from:'Νεο Κοσμο' ,
          to : 'Φιξ' ,
        }
      ] ,
    }
  } ,
  computed : {
    stop() {
      return this.stops.find(stop => stop.id == this.id)
    } ,
    route () {
      return this.routes.filter(route => route.idStop == this.stop.id)
    }
  }

}
</script>


<style scoped>
</style>
