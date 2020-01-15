<template lang="html">
  <v-container>
  <v-row align="center">
    <v-col class="text-center" cols="12" sm="4">
        <v-row>
            <v-col cols="12">
              <v-select v-model="cardType" :items="cardTypes" label="Επιλέξτε τύπο προϊόντος" @change="HandleCardChange(cardTypes)"></v-select>
            </v-col>
        </v-row>
        <v-row>
            <TicketCounter/>
        </v-row>
    </v-col>
    <v-col class="text-center" cols="12" sm="4">
      <template v-if="cardType=='Απλό εισητήριο'">
          <TicketTypes />
      </template>
      <template v-if="cardType=='Προσωποποιημένη κάρτα'">
        <v-form name="personal" v-model="klpaips">
            <template>
                <TicketTypes />
            </template>

        </v-form>
      </template>
      <template v-if="cardType=='Απρόσωπη κάρτα'">
        <v-form name="unpersonal" v-model="valid">
            <template>
            </template>
        </v-form>
      </template>
    </v-col>
  </v-row>

  </v-container>
</template>
<script>
import TicketTypes from "../components/Tickets/TicketTypes"
import TicketCounter from "../components/Tickets/TicketCounter"
export default{
    data:()=>({
        amount:0,
        product:"",
        cardType:"",
        cardTypes:[
            'Απλό εισητήριο',
            'Απρόσωπη κάρτα',
        ],

    }),
    components : {
        TicketTypes ,
        TicketCounter
    },
    methods:{
        minusone(){
            if(this.amount>0)
                this.amount--;
        },
        addone(){
            this.amount++;
        },
        submit(){
        }
    //HandleCardChange: function(evt){
    //    if(evt == 'Προσωποποιημένη κάρτα'){
    //    }
    //}
    },

}

</script>

<style lang="css" scoped>
</style>
