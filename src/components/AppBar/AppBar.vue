<template lang="HTML">
    <div>
    <v-app-bar
            app
            color="blue darken-3"
            dark
            height="80"
            hide-on-scroll

    >
        <v-container class="p-0 m-0"  fluid  >
            <v-row  align="center"  dense >
                <v-col class="hidden-md-and-up" cols="auto">
                    <v-app-bar-nav-icon @click.stop="drawer=!drawer"/>
                </v-col>
                <v-col cols="auto" >
                    <v-btn to="/" text color="transparent">
                        <v-img
                                class="shrink mr-2  flex-fill"
                                contain

                                src="../../assets/oasaLogo.png"



                                transition="scale-transition"
                                width="40"

                        />
                    </v-btn>

                </v-col>
                <v-col cols="auto" class="hidden-sm-and-down">
                    <v-btn text to="/maps/bus">
                        {{ $t("text.route")}}
                    </v-btn>
                </v-col>
                <v-col cols="auto" class="hidden-sm-and-down">
                    <v-btn text to="/tickets">
                        {{ $t("text.tickets")}}
                    </v-btn>
                </v-col>
                <v-col cols="auto" class="hidden-sm-and-down" >
                    <v-btn text to="/contact" >
                        {{ $t("text.contact")}}
                    </v-btn>
                </v-col>
                <v-col cols="auto" class="hidden-sm-and-down">
                    <v-btn text to="/about">
                        {{ $t("text.about")}}
                    </v-btn>
                </v-col>

                <v-spacer/>
                <v-col cols="auto" class="hidden-xs-only" v-if="!isLoggedIn">
                    <v-btn text outlined to="/signup"> {{ $t("text.signup")}}</v-btn>
                </v-col>
                <v-col cols="auto" class="hidden-xs-only" v-if="!isLoggedIn" >
                    <v-btn text outlined to="/login">{{ $t("text.login")}}</v-btn>
                </v-col>
                <v-col cols="auto"  class="hidden-xs-only" v-if="isLoggedIn"  >
                    <v-btn text outlined to="/profile/edit">Hi {{user.first_name}} !</v-btn>
                </v-col>
                <v-col cols="auto"  class="hidden-xs-only" v-if="isLoggedIn" >
                    <v-btn text outlined @click="doLogout">Logout</v-btn>
                </v-col>

                <v-col cols="1" class="hidden-xs-only">
                    <v-text-field
                            append-icon="fas fa-search"
                            label="Search"
                            single-line
                            hide-details
                    />
                </v-col>

                <v-col cols="1" >
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
    <v-navigation-drawer app disable-resize-watcher
                         absolute
                         temporary
                         v-model="drawer"
                         color="blue darken-3"
                         width="auto"


    >
        <v-list

        >
            <v-list-item-group

            >
                <v-list-item>
                    <v-list-item-title >
                        <router-link  class="white--text" style="text-transform: uppercase;text-decoration: none" to="/maps/bus">
                            {{ $t("text.route")}}
                        </router-link>
                    </v-list-item-title>
                </v-list-item>

                <v-list-item>
                    <v-list-item-title>
                        <router-link class="white--text" style="text-transform: uppercase;text-decoration: none" to="/tickets" >
                            {{ $t("text.tickets")}}
                        </router-link>
                    </v-list-item-title>
                </v-list-item>

                <v-list-item>
                    <v-list-item-title>
                        <router-link  class="white--text" style="text-transform: uppercase;text-decoration: none" to="/contact" >
                            {{ $t("text.contact")}}
                        </router-link>
                    </v-list-item-title>
                </v-list-item>

                <v-list-item>
                    <v-list-item-title>
                        <router-link  class="white--text" style="text-transform: uppercase;text-decoration: none"  to="/about"  >
                            {{ $t("text.about")}}
                        </router-link>
                    </v-list-item-title>
                </v-list-item>
                <v-list-item class="hidden-sm-and-up" v-if="!isLoggedIn">
                    <v-list-item-title>
                        <router-link   class="white--text" style="text-transform: uppercase;text-decoration: none"  to="/signup" >
                            {{ $t("text.signup")}}
                        </router-link>
                    </v-list-item-title>
                </v-list-item>
                <v-list-item class="hidden-sm-and-up" v-if="!isLoggedIn" >
                    <v-list-item-title>
                        <router-link  class="white--text" style="text-transform: uppercase;text-decoration: none"  to="/login" >
                            {{ $t("text.login")}}
                        </router-link>
                    </v-list-item-title>
                </v-list-item>
                <v-list-item class="hidden-sm-and-up">
                    <v-list-item-title v-if="isLoggedIn">
                        <router-link   class="white--text" style="text-transform: uppercase;text-decoration: none"  to="/profile/edit" >
                            Hi {{user.first_name}} !
                        </router-link>
                    </v-list-item-title>
                </v-list-item>
                <v-list-item class="hidden-sm-and-up">
                    <v-list-item-title v-if="isLoggedIn">
                        <span  @click="doLogout"  class="white--text" style="text-transform: uppercase;text-decoration: none"   >
                            Logout
                        </span>
                    </v-list-item-title>
                </v-list-item>
            </v-list-item-group>
        </v-list>

    </v-navigation-drawer>
    </div>

</template>

<script>

    import Route from "../StationInfo/Route/Route";
    export default {
        name: "AppBar",
        components: {Route},
        data(){
            return{
                languages:[
                  { text : 'Greek' , value : 'gr'} ,
                  { text : 'English' , value : 'en'} ,
                ] ,
                select : '',
                drawer:false
            }
        } ,
        computed : {
          isLoggedIn() {
            if (this.$store.state.token) {
              return true
            }
            return false  ;
          } ,
          user() {
            return this.$store.state.user ;
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
