<template>
  <v-container >
    <v-row>
    <v-card
        class="mt-12 mx-auto"
        color="rgb(48, 48, 48)"
        cols="12" sm="10" md="10"
        
    >
    <v-card-title class="headline" >Login</v-card-title>
     <v-card-text>
      <v-col cols="12">
        <v-col cols="12" sm="8" md="10">
          <v-text-field v-model="userAccount.username"
            placeholder="username"
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="8" md="10">
          <v-text-field
            v-model="userAccount.password"
            :append-icon="showPasswd ? 'mdi-eye' : 'mdi-eye-off'"
            :type="showPasswd ? 'text' : 'password'"
            name="input-10-1"
            label="Password"
            counter
            @click:append="showPasswd = !showPasswd"
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="10" md="12">
            <v-btn large color="primary" @click="login2Dsh()">Login</v-btn>
        </v-col>
        <!-- <v-col cols="12" sm="10" md="12">
            <v-btn large color="primary" @click="authorization('engineer');login2Dsh()">Engineer View</v-btn>
            <v-btn large color="primary" @click="authorization('reviewer');login2Dsh()">Reviewer View</v-btn>
        </v-col> -->
      </v-col>
     </v-card-text>
    </v-card>

    </v-row>
  </v-container>  
</template>
<script>
export default {
    data:()=>({
        showPasswd: false,
        userAccount: {
          username: null,
          password: null,
        }
    }),
    methods: {
      login2Dsh() {
        this.$store.commit('setAccount', this.userAccount)
        setTimeout(() => {
          this.$router.push(`/dashboard`)
        }, 3000);
      },
      authorization(role) {
        this.$store.commit(role)
      }
    },
}
</script>