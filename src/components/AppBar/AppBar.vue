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
                    <v-btn text>
                        Routes
                    </v-btn>
                </v-col>
                <v-col cols="auto">
                    <v-btn text>
                        Tickets
                    </v-btn>
                </v-col>
                <v-col cols="auto"  >
                    <v-btn text >
                        Contact
                    </v-btn>
                </v-col>
                <v-col cols="auto" >
                    <v-btn text >
                        About us
                    </v-btn>
                </v-col>

                <v-spacer/>
                <v-col cols="auto"  >
                    <v-btn text outlined to="/signup"> Sign Up </v-btn>
                </v-col>
                <v-col cols="auto" >
                    <v-btn text outlined to="/login"> Login</v-btn>
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
                            label="select lunguage"
                            height="54"
                            single-line
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
                    "Greek","English"
                ]
            }
        }
    }
</script>

<style scoped>

</style>
