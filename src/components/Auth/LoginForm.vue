<template>
  <div class="">
    <v-container >
    <v-layout row>
      <v-flex sm2 md2 lg2>
        <v-spacer></v-spacer>
      </v-flex>
      <v-flex sm8 md8 lg8>
        <v-card tile>
          <v-card-title class="justify-center">
            <v-img
              src="https://www.newsit.gr/wp-content/uploads/2017n/10/karta-2-768x512.jpg"
              height="200"
              gradient="to top right, rgba(100,115,201,.33), rgba(25,32,72,.7)"
              >
            </v-img>
          </v-card-title >
          <v-card-title class="justify-center">Εισοδος
            <v-icon>
              mdi-account
            </v-icon>
          </v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <v-form >
              <validation-provider rules="required" v-slot="{ errors }">
                <v-text-field

                  v-model="email"
                  label="Email"
                  v-on:keyup.enter.native="showPassword"

                >
                </v-text-field>
                <span>{{ errors[0] }}</span>
              </validation-provider>
              <validation-provider rules="required" v-slot="{ errors }">
                <v-text-field

                  v-model="password"
                  label="Password"
                  append-icon="mdi-eye-off"
                  type="password"
                  v-show="hiddenPassword"
                  @keyup.enter="handleSubmit()"
                >
                </v-text-field>
                <span>{{ errors[0] }}</span>
                <v-btn
                @click="showPassword"

                v-show="hiddenCont"
                >Συνεχεια</v-btn>
              </validation-provider>
              <v-btn
                @click="handleSubmit()"
                v-show="hiddenPassword"
                >Εισοδος</v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-flex>
      <v-flex sm2 md2 lg2>
        <v-spacer></v-spacer>
      </v-flex>
    </v-layout>
    </v-container>
  </div>
</template>

<script>
import { extend } from 'vee-validate';
import { required } from 'vee-validate/dist/rules';
import { ValidationProvider } from 'vee-validate';

extend('required', {
  ...required,
  message: 'This field is required'
});
export default {
  name : 'LoginForm' ,
  components : {
    ValidationProvider
  },
  data () {
    return {
      email : '' ,
      password : '' ,
      hiddenPassword : false ,
      hiddenCont : true
    }
  } ,
  methods : {
    handleSubmit() {
      console.log(this.email,this.password);
    } ,
    showPassword() {
      this.hiddenPassword = true ;
      this.hiddenCont = false ;
    }
  }
}
</script>
<style lang="css" scoped>
</style>
