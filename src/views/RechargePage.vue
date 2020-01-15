<template lang="html">
  <v-container>
      <v-row align="center">
          <v-col>
            <TicketTypes :disabled="false" />
          </v-col>
          <v-col>
             <BillingInfo />
          </v-col>
      </v-row>
  </v-container>
</template>
<script>
import TicketTypes from "../components/Tickets/TicketTypes"
import BillingInfo from "../components/Tickets/BillingInfo"
export default{
    data:()=>({
        product:"",
        cardType:"",
        cardTypes:[
            'Προσωποποιημένη κάρτα',
        ],

    }),
    components : {
        TicketTypes ,
        BillingInfo
    },
    methods:{
        submit(){
            this.$router.push("checkout");
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
