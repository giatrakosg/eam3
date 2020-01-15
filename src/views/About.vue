<template>
    <v-card>
        <v-card-title style="color:#1565C0;">
            Public Transport Operators
        </v-card-title>
        <v-divider style="color: #004B84" />

        <v-card-text>

            <v-list-item three-line>
                <v-list-item-avatar
                        tile
                        size="100"

                >
                    <v-img src="../assets/smedia_logo1.jpg"/>
                </v-list-item-avatar>
                <v-list-item-content>
                    <v-list-item-title class=" mb-1"><a href="http://www.osy.gr/">ODIKES SYNGKOINONIES S.A. </a> </v-list-item-title>
                    <v-list-item-subtitle>

                        <v-container class="mt-2">
                            <v-row>
                                <v-col cols="auto">
                                    <div >
                                        Parnassou 6 - 182-33 Aghios Ioannis Rentis
                                    </div>
                                    <div class="mt-1">
                                        Τel. 210 4270796
                                    </div>
                                    <div class="mt-1">
                                        E-mail: ethelbus@ethel.gr
                                    </div>

                                </v-col>
                                <v-col cols="1">
                                    <v-img src="../assets/bus.png" width="60" />
                                </v-col>
                                <v-col cols="1">
                                    <v-img src="../assets/trolley.png" width="60" />
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-list-item-subtitle>
                    <div class="mt-0">
                        The company ODIKES SYGKOINONIES SA with the distinctive title “OSY” resulted from the merging of ETHEL SA and ILPAP SA. OSY S.A. is a subsidiary company of OASA and aims at the operation and exploitation of the transport services provided by thermal and trolley buses in the metropolitan area of Athens
                    </div>

                </v-list-item-content>


            </v-list-item>
            <v-list-item three-line>
                <v-list-item-avatar
                        tile
                        size="100"

                >
                    <v-img src="../assets/stasy.png"/>
                </v-list-item-avatar>
                <v-list-item-content>
                    <v-list-item-title class=" mb-1"><a href="http://www.stasy.gr/">STASY S.A.</a> </v-list-item-title>
                    <v-list-item-subtitle>
                        <v-container class="mt-2">
                            <v-row>
                                <v-col cols="auto">
                                    <div >
                                        Athinas 67 - 105-52 Athens
                                    </div>
                                    <div class="mt-1">
                                        Τel.: 210 3248311-17, 210-5194012 Fax: 210 3223935
                                    </div>
                                    <div class="mt-1">
                                        E-mail: pservice@ametro.gr
                                    </div>

                                </v-col>
                                <v-col cols="1">
                                    <v-img src="../assets/metro.png" width="60" />
                                </v-col>
                                <v-col cols="1">
                                    <v-img src="../assets/tram.png" width="60" />
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-list-item-subtitle>
                    <div class="mt-0">
                        The company STATHERES SYNGKOINONIES SA with the distinctive title STASY resulted from the merging of AMEL SA, ISAP SA and TRAM SA. STASY S.A. is a subsidiary company of OASA and aims at the operation and exploitation of the transport services provided by the metro, electric railways and tram in the metropolitan area of Athens
                    </div>

                </v-list-item-content>


            </v-list-item>
        </v-card-text>
    </v-card>
</template>

<script>
    export default {
        name: "About"
    }
</script>

<style scoped>

</style>