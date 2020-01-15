<template lang="html">
  <v-container>
  <v-row align="center">
    <v-col class="text-center" cols="12" sm="4">
      <v-col cols="12">
        <v-select v-model="cardType" :items="cardTypes" label="Επιλέξτε τύπο προϊόντος" @change="HandleCardChange(cardTypes)"></v-select>
      </v-col>
      <v-btn @click="minusone">
        <v-icon>mdi-minus-box</v-icon></v-btn>
        {{this.amount}}<v-btn @click="addone">
        
        <v-icon>mdi-plus-box</v-icon></v-btn>
    </v-col>
    <v-col class="text-center" cols="12" sm="4">
      <h1>Προϊόντα</h1>
      <template v-if="cardType=='Απλό εισητήριο'">
        <v-form name="simple" v-model="product">
            <v-radio-group v-model="product" :mandatory="false">
                <v-radio label="1 εισητήριο 90 λεπτών" value="one"></v-radio>
                <v-radio label="5 εισητήρια 90 λεπτών" value="five"></v-radio>
                <v-radio label="10+1 εισητήρια 90 λεπτών" value="ten"></v-radio>
                <v-radio label="1 ημέρας" value="day"></v-radio>
                <v-radio label="5 ημέρων" value="week"></v-radio>
                <v-radio label="30 ημέρων" value="month"></v-radio>
        </v-radio-group>
            <v-btn class="mr-4" @click.stop.prevent="submit()">Submit</v-btn>
        </v-form>
        
        
      </template>
      <template v-if="cardType=='Προσωποποιημένη κάρτα'">
        <v-form name="personal" v-model="klpaips">
            <template>
                
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
    methods:{
        minusone(){
            if(this.amount>0)
                this.amount--;
        },
        addone(){
            this.amount++;
        },
        submit(){
            sessionStorage.setItem('product', this.product);
            sessionStorage.setItem('cardType', this.cardType);
            sessionStorage.setItem('amount', this.amount);
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
