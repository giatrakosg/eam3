<template>
  <div class="">
    <v-container >
    <v-layout row>
      <v-flex sm2 md2 lg2>
        <v-spacer></v-spacer>
      </v-flex>
      <v-flex sm8 md8 lg8>
        <v-card>
          <v-card-title>Εισοδος</v-card-title>
          <v-card-text>
            <v-form >
              <validation-provider rules="required" v-slot="{ errors }">
                <v-text-field solo v-model="name" label="Name">
                </v-text-field>
                <span>{{ errors[0] }}</span>
              </validation-provider>
              <validation-provider rules="required" v-slot="{ errors }">
                <v-text-field solo v-model="password" label="Password">
                </v-text-field>
                <span>{{ errors[0] }}</span>
              </validation-provider>
              <v-btn @click="handleSubmit()">Εισοδος</v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-flex>
      <v-flex sm2 md2 lg2>
        <v-spacer></v-spacer>
      </v-flex>
    </v-layout>
    <v-layout row>
      <v-flex sm2 md2 lg2>
        <v-spacer></v-spacer>
      </v-flex>
      <v-flex sm8 md8 lg8>
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
      name : '' ,
      password : ''
    }
  } ,
  methods : {
    handleSubmit() {
      console.log(this.name,this.password);
    }
  }
}
</script>
<style lang="css" scoped>
</style>
