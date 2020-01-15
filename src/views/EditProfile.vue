<template lang="html">
  <v-container>
      <v-card>
          <v-card-title>Profile</v-card-title>
      </v-card>
     <v-row >
       <v-col  >
         <v-card
         tile
         >
           <v-list-item three-line>
             <v-list-item-avatar

             >
               <v-avatar color="indigo">
                 <v-icon dark>mdi-account-circle</v-icon>
               </v-avatar>
             </v-list-item-avatar>
             <v-list-item-content>

               <v-list-item-title class="headline mb-1">Emilia Emilia </v-list-item-title>
               <v-list-item-subtitle>Student</v-list-item-subtitle>
             </v-list-item-content>
           </v-list-item>
         </v-card>
       </v-col>
       <v-col >
         <v-card

                 tile
         >
           <v-list-item three-line>
             <v-list-item-avatar

             >
               <v-avatar >
               <i class="fas fa-id-card fa-2x " style="color: #1DA1F2" />
               </v-avatar>
             </v-list-item-avatar>
             <v-list-item-content>
               <v-list-item-title class="headline mb-1">CARD ID:12345678 </v-list-item-title>
               <v-list-item-subtitle>Valid Till:     11/22</v-list-item-subtitle>
             </v-list-item-content>
           </v-list-item>
         </v-card>
       </v-col>
     </v-row>
    <v-row>
      <v-col>
        <EditProfileForm/>
      </v-col>
      <v-col>
        <CardInfo/>

      </v-col>
    </v-row>

    </v-container>
</template>
<script>
import EditProfileForm from "../components/EditProfile/EditProfileForm";
import CardInfo from "../components/EditProfile/CardInfo";
export default {
  name : 'EditProfile',
  components: {CardInfo, EditProfileForm}
}
</script>

<style lang="css" scoped>
</style>
