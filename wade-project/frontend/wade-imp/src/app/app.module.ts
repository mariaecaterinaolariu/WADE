import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { UploadService } from './features/upload/upload.service';
import { UploadComponent } from './features/upload/upload.component';
import { HttpClientModule } from '@angular/common/http';
import { PortraitsComponent } from './features/portraits/portraits.component';
import { PortraitsService } from './features/portraits/portraits.service';
import { Base64Pipe } from './shared/pipes/convert-base64.pipe';

@NgModule({
  declarations: [
    AppComponent,
    UploadComponent,
    PortraitsComponent,
    Base64Pipe
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule 
  ],
  providers: [
    UploadService,
    PortraitsService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
