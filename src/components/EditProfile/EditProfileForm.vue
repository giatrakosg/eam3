<template>
    <v-card tile>
        <v-toolbar
          flat
          color="primary"
        >
          <v-icon>mdi-account</v-icon>
          <v-toolbar-title class="font-weight-light">User Profile</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn
            color="success"
            fab
            small
            @click="isEditing = !isEditing"
          >
            <v-icon v-if="isEditing">mdi-close</v-icon>
            <v-icon v-else>mdi-pencil</v-icon>
          </v-btn>
        </v-toolbar>
        <v-divider></v-divider>
        <v-card-text>
            <v-form >
                <v-row>
                    <v-col>
                        <validation-provider rules="required" v-slot="{ errors }">
                            <v-text-field
                                    v-model="user.first_name"
                                    label="Name"
                                    v-on:keyup.enter.native="showPassword"
                                    :disabled="!isEditing"
                            >
                            </v-text-field>
                        </validation-provider>
                    </v-col>
                    <v-col>
                        <validation-provider rules="required" v-slot="{ errors }">
                            <v-text-field
                                    v-model="user.last_name"
                                    label="Surname"
                                    v-on:keyup.enter.native="showPassword"
                                    :disabled="!isEditing"
                            >
                            </v-text-field>
                        </validation-provider>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <validation-provider rules="required" v-slot="{ errors }">
                            <v-text-field
                                    v-model="user.email"
                                    label="Email.."
                                    v-on:keyup.enter.native="showPassword"
                                    append-icon="mdi-email"
                                    :disabled="!isEditing"
                            >
                            </v-text-field>
                            <span>{{ errors[0] }}</span>
                        </validation-provider>
                    </v-col>
                </v-row>
                <validation-provider rules="required" v-slot="{ errors }">
                    <v-text-field
                            v-model="user.phone"
                            label="Telephone.."
                            append-icon="mdi-cellphone"
                            type="number"
                            @keyup.enter="handleSubmit()"
                            :disabled="!isEditing"
                    >
                    </v-text-field>
                    <span>{{ errors[0] }}</span>
                </validation-provider>
                <v-btn
                        @click="handleSubmit()"
                        block
                        color="success"
                >SAVE</v-btn>
            </v-form>
        </v-card-text>
    </v-card>
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
        name : 'EditProfileForm' ,
        components : {
            ValidationProvider
        },
        data () {
            return {
                isEditing : false
            }
        },
        methods : {
            handleSubmit() {
               // console.log(this.email,this.password);
                let data = {
                    first_name: this.user.first_name,
                    last_name : this.user.last_name ,
                    email: this.user.email,
                    password: this.password,
                    phone : this.tel
                };
                this.$store
                    .dispatch("update", data)
                    .then(() => this.$router.push("/"))
            } ,
            changeEditing() {
                this.isEditing = !this.isEditing ;
            }
        },
        computed:{
            user(){
                return this.$store.state.user;
            }
        }

    }
</script>
<style lang="css" scoped>
</style>
