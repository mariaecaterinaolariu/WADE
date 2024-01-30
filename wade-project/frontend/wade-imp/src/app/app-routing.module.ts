import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UploadComponent } from './features/upload/upload.component';
import { PortraitsComponent } from './features/portraits/portraits.component';

const routes: Routes = [
  { path: 'upload', component: UploadComponent },
  { path: 'portraits', component: PortraitsComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
