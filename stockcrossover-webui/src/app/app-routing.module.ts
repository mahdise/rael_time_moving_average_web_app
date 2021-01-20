import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { ShowtableComponent } from './showtable/showtable.component';

const routes: Routes = [
  { path: "", redirectTo: "/showtable", pathMatch: "full" },
  {
    path: "showtable",
    component: ShowtableComponent,
  },
  {
    path: "login",
    component: LoginComponent,
  }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
