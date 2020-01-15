<template>
    <v-card tile>
        <v-card-title class="justify-center">
          Edit Profile:
        </v-card-title>
        <v-divider></v-divider>
        <v-card-text>
            <v-form >
                <v-row>
                    <v-col>
                        <validation-provider rules="required" v-slot="{ errors }">
                            <v-text-field

                                    v-model="this.user.username"
                                    label="Name"
                                    v-on:keyup.enter.native="showPassword"

                            >
                            </v-text-field>
                        </validation-provider>
                    </v-col>
                    <v-col>
                        <validation-provider rules="required" v-slot="{ errors }">
                            <v-text-field
                                    v-model="this.user.last_name"
                                    label="Surname"
                                    v-on:keyup.enter.native="showPassword"
                            >
                            </v-text-field>
                        </validation-provider>
                    </v-col>
                    <v-col>
                        <validation-provider rules="required" v-slot="{ errors }">
                            <v-text-field
                                    v-model="user.email"
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
                                    v-model="user.password"
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
                                    v-model="user.passwordRetype"
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
                            v-model="user.tel"
                            label="Telephone.."
                            append-icon="mdi-cellphone"
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
        methods : {
            handleSubmit() {
               // console.log(this.email,this.password);
                let data = {
                    name: this.username,
                    first_name: this.username,
                    last_name : this.surname ,
                    email: this.email,
                    password: this.password,
                    phone : this.tel
                };
                this.$store
                    .dispatch("update", data)
                    .then(() => this.$router.push("/"))


            } ,
        },
        computed:{
            user(){
                return {"firstname": this.$store.state.user.first_name};
            }
        }

    }
</script>
<style lang="css" scoped>
</style>
