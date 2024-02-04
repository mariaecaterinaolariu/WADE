import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UploadComponent } from './features/upload/upload.component';
import { PortraitsComponent } from './features/portraits/portraits.component';
import { PaintersComponent } from './features/painters/painters.component';
import { AppComponent } from './app.component';
import { HomeComponent } from './core/home/home/home.component';

const routes: Routes = [
  {path: '', component: PortraitsComponent},
  { path: 'upload', component: UploadComponent },
  { path: 'portraits', component: PortraitsComponent },
  {path: 'painters/:name', component: PaintersComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
