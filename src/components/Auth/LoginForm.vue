<template>
  <div class="">
    <v-layout row>
      <v-flex sm2 md2 lg2>
        <v-spacer></v-spacer>
      </v-flex>
      <v-flex sm8 md8 lg8>
        <validation-provider rules="required" v-slot="{ errors }">
          <v-text-field solo v-model="name">
          </v-text-field>
          <span>{{ errors[0] }}</span>
        </validation-provider>
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
        <validation-provider rules="required" v-slot="{ errors }">
          <v-text-field solo v-model="password">
          </v-text-field>
          <span>{{ errors[0] }}</span>
        </validation-provider>
      </v-flex>
      <v-flex sm2 md2 lg2>
        <v-spacer></v-spacer>
      </v-flex>
    </v-layout>
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
      value : ''
    }
  }
}
</script>
<style lang="css" scoped>
</style>
