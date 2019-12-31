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
                  <v-list-item-title class="headline mb-1">{{routes[0].direction}}</v-list-item-title>
                  <v-list-item-subtitle>Απο : {{routes[0].from}}</v-list-item-subtitle>
                  <v-list-item-subtitle>Προς : {{routes[0].to}}</v-list-item-subtitle>
                </v-list-item-content>

                <v-list-item-avatar
                  raised
                  size="80"
                  color="primary"
                >136</v-list-item-avatar>
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
          :to="'/bus/route/' + this.id"
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
  name : 'RouteInfoCard' ,
  props : ['id'] ,
  data() {
    return {
      routes : [
        {
          id:2,
          number:136,
          direction:'Προς Στ. Φιξ',
          from:'Νεα Σμυρνη' ,
          to : 'Φιξ' ,
          stations :
            [
              {id : 0 , name : 'Ευαγγελικη' },
              {id : 1 , name : 'Αιγαιου 1' },
              {id : 2 , name : 'Αιγαιου 3' },
              {id : 3 , name : 'Εφεσου' },
              {id : 4 , name : 'Παντειος' },
              {id : 5 , name : 'Φιξ' }

            ]} ,
        {
          id:3,
          number:136,
          direction:'Προς Συνταγμα',
          from:'Νεο Κοσμο' ,
          to : 'Φιξ' ,
          stations :
          [
            {id : 0 , name : 'Ευαγγελικη'},
            {id : 1 , name : 'Αιγαιου 1'},
            {id : 2 , name : 'Αιγαιου 3'},
            {id : 3 , name : 'Εφεσου'},
            {id : 4 , name : 'Παντειος'},
            {id : 5 , name : 'Φιξ'}
          ]}
      ] ,


      stations : [
        {id : 0 , name : 'ev'},
        {id : 1 , name : 'ag 1'},
        {id : 2 , name : 'ag 3'},
        {id : 3 , name : 'ef'},
        {id : 4 , name : 'pa'},
        {id : 5 , name : 'f'} ,
      ] ,
      headers :
        [
          {text : 'id' , value : 'id'},
          {text : 'name' , value : 'name'},

        ]
       ,

    }
  } ,
  computed : {
    points () {
      let route = this.routes[0];
      let positions = [];
      for (var i = 0; i < route.stations.length; i++) {
        positions.push({ id : route.stations[i].id , position : route.stations[i].position });
      }
      return positions ;
    },
    positions () {
      let route = this.routes[0];
      let positions = [];
      for (var i = 0; i < route.stations.length; i++) {
        positions.push(route.stations[i].position );
      }
      return positions ;

    }
  }

}
</script>


<style scoped>
</style>
