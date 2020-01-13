<template>
   <v-footer
           style="width: 100%"
           padless
   >
      <v-card
              color="blue darken-3"
              width="100%"

      >
         <v-card-text >
            <v-container >
               <v-row justify="center" >
                  <v-col >
                     <v-list dense color="transparent" >
                        <v-subheader  style="color: whitesmoke"> {{$t('text.terms_and_policies')}} </v-subheader>
                        <v-divider style="background-color: whitesmoke"/>
                     <v-list-item-group color="primary" >
                        <v-list-item
                        >
                           <v-list-item-content>
                              <v-list-item-title  style="color: whitesmoke"> {{$t('text.terms_of_use')}}</v-list-item-title>
                           </v-list-item-content>
                        </v-list-item>
                        <v-list-item
                        >

                           <v-list-item-content>
                              <v-list-item-title style="color: whitesmoke"> {{$t('text.personal_data_policies')}}</v-list-item-title>
                           </v-list-item-content>
                        </v-list-item>
                        <v-list-item
                        >

                           <v-list-item-content>
                              <v-list-item-title style="color: whitesmoke"> {{$t('text.cookies_policies')}}</v-list-item-title>
                           </v-list-item-content>
                        </v-list-item>
                     </v-list-item-group>
                  </v-list>
                  </v-col>
                  <v-col>
                     <v-list dense color="transparent" >
                        <v-subheader  style="color: whitesmoke"> {{$t('text.news')}} </v-subheader>
                        <v-divider style="background-color: whitesmoke"/>
                        <v-list-item-group color="primary" >
                           <v-list-item
                           >
                              <v-list-item-content>
                                 <v-list-item-title  style="color: whitesmoke"> {{$t('text.press_releases')}}</v-list-item-title>
                              </v-list-item-content>
                           </v-list-item>
                           <v-list-item
                           >

                              <v-list-item-content>
                                 <v-list-item-title style="color: whitesmoke"> {{$t('text.announcements')}}</v-list-item-title>
                              </v-list-item-content>
                           </v-list-item>

                        </v-list-item-group>
                     </v-list>
                  </v-col>
                  <v-col>
                     <v-list dense color="transparent" >
                        <v-subheader  style="color: whitesmoke"> {{$t('text.public_tendering')}} </v-subheader>
                        <v-divider style="background-color: whitesmoke"/>
                        <v-list-item-group color="primary" >
                           <v-list-item
                           >
                              <v-list-item-content>
                                 <v-list-item-title  style="color: whitesmoke"> {{$t('text.job_openings')}}</v-list-item-title>
                              </v-list-item-content>
                           </v-list-item>
                           <v-list-item
                           >

                              <v-list-item-content>
                                 <v-list-item-title style="color: whitesmoke"> {{$t('text.intrships')}}</v-list-item-title>
                              </v-list-item-content>
                           </v-list-item>
                           <v-list-item
                           >

                              <v-list-item-content>
                                 <v-list-item-title style="color: whitesmoke"> {{$t('text.public_tendering')}}</v-list-item-title>
                              </v-list-item-content>
                           </v-list-item>

                        </v-list-item-group>
                     </v-list>
                  </v-col>
                  <v-col>
                     <v-list dense color="transparent" >
                        <v-subheader  style="color: whitesmoke"> {{$t('text.contact')}} </v-subheader>
                        <v-divider style="background-color: whitesmoke"/>
                        <v-list-item-group color="primary" >
                           <v-list-item
                           >
                              <v-list-item-content>
                                 <v-list-item-title  style="color: whitesmoke"> {{$t('text.complaints')}}</v-list-item-title>
                              </v-list-item-content>
                           </v-list-item>

                           <v-list-item
                           >

                              <v-list-item-content>
                                 <v-list-item-title style="color: whitesmoke"> {{$t('text.links')}}</v-list-item-title>
                              </v-list-item-content>
                           </v-list-item>

                        </v-list-item-group>
                     </v-list>
                  </v-col>
               </v-row>
            </v-container>
         </v-card-text>

         <v-divider/>

         <v-card-text class="white--text text-center">
            <strong>2020 (c) OASA </strong>
         </v-card-text>
      </v-card>
   </v-footer>
</template>

<script>
    export default {
        name: "Footer"
    }
</script>

<style scoped>



</style>