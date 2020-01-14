<template lang="html">
  <v-container>
  <v-row align="center">
    <v-col class="text-center" cols="12" sm="4">
      <v-col cols="12">
        <v-select v-model="cardType" :items="cardTypes" label="Επιλέξτε τύπο προϊόντος" @change="HandleCardChange(cardTypes)"></v-select>
        <template v-if="cardType == 'Προσωποποιημένη κάρτα'">
        <v-form name="persona" v-model="valid">
            <v-text-field v-model="firstname" :rules="nameRules" :counter="60" label="First name" required>
            </v-text-field>
            <v-text-field v-model="lastname" :rules="nameRules" :counter="60" label="Last name" required>
            </v-text-field>
            <v-text-field v-model="realaddress" :rules="nameRules" :counter="90" label="Address" required>
            </v-text-field>
            <v-text-field v-model="email" :rules="emailRules" :counter="90" label="E-Mail">
            </v-text-field>
            <v-text-field v-model="pin" :rules="numberRules" :counter="8" label="PIN" required>
            </v-text-field>
            <v-text-field v-model="AMKA" :rules="numberRules" :counter="11" label="AMKA" required>
            </v-text-field>
        </v-form>
        </template>
        <template v-if="cardType != 'Προσωποποιημένη κάρτα'">
            
        </template>
      </v-col>
    </v-col>
    <v-col class="text-center" cols="12" sm="4">
      <h1>Προϊόντα</h1>
      <template v-if="cardType=='Απλό εισητήριο'">
        <v-form name="simple" v-model="valid">
            <v-radio-group v-model="product" :mandatory="false">
                <v-radio label="1 εισητήριο 90 λεπτών" value="one"></v-radio>
                <v-radio label="5 εισητήρια 90 λεπτών" value="five"></v-radio>
                <v-radio label="10+1 εισητήρια 90 λεπτών" value="ten"></v-radio>
                <v-radio label="1 ημέρας" value="day"></v-radio>
                <v-radio label="5 ημέρων" value="week"></v-radio>
                <v-radio label="30 ημέρων" value="month"></v-radio>
        </v-radio-group>

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
sessionStorage.setItem("total",120);
export default{
    data:()=>({
        simple_num:0,
        product:"",
        cardType:"",
        cardTypes:[
            'Απλό εισητήριο',
            'Προσωποποιημένη κάρτα',
            'Απρόσωπη κάρτα',
        ],
        
    }),
    methods:{
    //HandleCardChange: function(evt){
    //    if(evt == 'Προσωποποιημένη κάρτα'){
    //    }
    //}
    },
    
}
</script>

<style lang="css" scoped>
</style>
