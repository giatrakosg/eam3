<template lang="HTML">
    <v-app-bar
            app
            color="blue darken-3"
            dark
            height="130"
            hide-on-scroll

    >
        <v-container class="p-0 m-0"  fluid  >
            <v-row  align="center"  dense >
                <v-col cols="auto" >
                    <v-btn href="/" text color="transparent">
                        <v-img
                                class="shrink mr-2  flex-fill"
                                contain

                                src="../../assets/oasaLogo.png"



                                transition="scale-transition"
                                width="40"

                        />
                    </v-btn>

                </v-col>
                <v-col cols="auto" >
                    <v-btn text to="/maps/bus">
                        {{ $t("text.route")}}
                    </v-btn>
                </v-col>
                <v-col cols="auto">
                    <v-btn text>
                        {{ $t("text.tickets")}}
                    </v-btn>
                </v-col>
                <v-col cols="auto"  >
                    <v-btn text href="/contact" style="text-decoration:none ">
                        {{ $t("text.contact")}}
                    </v-btn>
                </v-col>
                <v-col cols="auto" >
                    <v-btn text >
                        {{ $t("text.about")}}
                    </v-btn>
                </v-col>

                <v-spacer/>
                <v-col cols="auto"  v-if="!isLoggedIn">
                    <v-btn text outlined to="/signup"> {{ $t("text.signup")}}</v-btn>
                </v-col>
                <v-col cols="auto"  v-if="!isLoggedIn" >
                    <v-btn text outlined to="/login">{{ $t("text.login")}}</v-btn>
                </v-col>
                <v-col cols="auto"  v-if="isLoggedIn" >
                    <v-btn text outlined to="/user/profile">Hi Emilia !</v-btn>
                </v-col>
                <v-col cols="auto"  v-if="isLoggedIn" >
                    <v-btn text outlined @click="doLogout">Logout</v-btn>
                </v-col>

                <v-col cols="1" class="d-sm-none d-md-flex">
                    <v-text-field
                            append-icon="fas fa-search"
                            label="Search"
                            single-line
                            hide-details
                    />
                </v-col>

                <v-col cols="1">
                    <v-select
                            :items="languages"
                            label="select language"
                            height="54"
                            v-model="select"
                            single-line
                            @change="setLanguage"
                    />
                </v-col>
            </v-row>
        </v-container>

    </v-app-bar>
</template>

<script>

    export default {
        name: "AppBar",
        data(){
            return{
                languages:[
                  { text : 'Greek' , value : 'gr'} ,
                  { text : 'English' , value : 'en'} ,
                ] ,
                select : ''
            }
        } ,
        computed : {
          isLoggedIn() {
            if (this.$store.state.token) {
              return true
            }
            return false  ;
          }
        } ,
        methods : {
          setLanguage() {
            //this.$store.setLanguage(this.select)
            this.$i18n.locale = this.select ;
            return this.$store.commit('setLanguage' ,
            {'lang' : this.select})
          } ,
          doLogout() {
            return this.$store.dispatch('logout')
          }
        }
    }
</script>

<style scoped>

</style>
