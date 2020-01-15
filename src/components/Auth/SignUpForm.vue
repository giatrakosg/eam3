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
              src="https://taxcoach.gr/wp-content/uploads/2018/01/athena-card.jpg"
              height="320"
              >
            </v-img>
          </v-card-title >
          <v-card-title class="justify-center">Εγγραφη χρηστη
            <v-icon>
              mdi-account
            </v-icon>
          </v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <v-form >
              <v-row>
                <v-col>
                  <validation-provider rules="required" v-slot="{ errors }">
                    <v-text-field

                      v-model="username"
                      label="Name"
                      v-on:keyup.enter.native="showPassword"

                    >
                    </v-text-field>
                  </validation-provider>
                </v-col>
                <v-col>
                  <validation-provider rules="required" v-slot="{ errors }">
                    <v-text-field
                      v-model="surname"
                      label="Surname"
                      v-on:keyup.enter.native="showPassword"
                    >
                    </v-text-field>
                  </validation-provider>
                </v-col>
                <v-col>
                  <validation-provider rules="required" v-slot="{ errors }">
                    <v-text-field
                      v-model="email"
                      label="Email.."
                      v-on:keyup.enter.native="showPassword"
                      append-icon="mdi-email"
                    >
                    </v-text-field>
                    <span>{{ errors[0] }}</span>
                  </validation-provider>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <validation-provider rules="required" v-slot="{ errors }">
                    <v-text-field
                      v-model="password"
                      label="Password"
                      append-icon="mdi-eye-off"
                      type="password"
                      @keyup.enter="handleSubmit()"
                    >
                    </v-text-field>
                    <span>{{ errors[0] }}</span>
                  </validation-provider>
                </v-col>
                <v-col>
                  <validation-provider rules="required" v-slot="{ errors }">
                    <v-text-field
                      v-model="passwordRetype"
                      label="Retype Password.."
                      append-icon="mdi-eye-off"
                      type="password"
                      @keyup.enter="handleSubmit()"
                    >
                    </v-text-field>
                    <span>{{ errors[0] }}</span>
                  </validation-provider>
                </v-col>
              </v-row>
              <validation-provider rules="required" v-slot="{ errors }">
                <v-text-field
                  v-model="tel"
                  label="Telephone.."
                  append-icon="mdi-cellphone"
                  type="number"
                  @keyup.enter="handleSubmit()"
                >
                </v-text-field>
                <span>{{ errors[0] }}</span>
              </validation-provider>
              <validation-provider rules="required" v-slot="{ errors }">
                <v-text-field
                  v-model="address"
                  label="Address"
                  @keyup.enter="handleSubmit()"
                >
                </v-text-field>
                <span>{{ errors[0] }}</span>
              </validation-provider>
              <validation-provider rules="required" v-slot="{ errors }">
                <v-text-field
                  v-model="AMKA_id"
                  label="AMKA"
                  type="number"
                  @keyup.enter="handleSubmit()"
                >
                </v-text-field>
                <span>{{ errors[0] }}</span>
              </validation-provider>
              <v-btn
                @click="handleSubmit()"
                block
                color="success"
                >Εγγραφη</v-btn>
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
  name : 'SignUpForm' ,
  components : {
    ValidationProvider
  },
  data () {
    return {
      email : '' ,
      password : '' ,
      passwordRetype : '',
      tel : '',
      username : '' ,
      surname : '',
      address: '',
      AMKA_id: ''
    }
  } ,
  methods : {
    handleSubmit() {
      console.log(this.email,this.password);
      let data = {
        name: this.username,
        first_name: this.username,
        last_name : this.surname ,
        email: this.email,
        password: this.password,
        phone : this.tel,
        address: this.address,
        AMKA_id: this.AMKA_id
      };
      this.$store
        .dispatch("register", data)
        .then(() => this.$router.push("/"))
        .catch(err => console.log(err));

    } ,
  }
}
</script>
<style lang="css" scoped>
</style>
